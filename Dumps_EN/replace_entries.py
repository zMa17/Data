#!/usr/bin/env python3
# replace_entries.py
# Usage:
#   python replace_entries.py source.xml translate.txt output.xml

import re
import sys
from pathlib import Path

def main():
    if len(sys.argv) < 4:
        print("Usage: python replace_entries.py source.xml translate.txt output.xml")
        sys.exit(1)

    source_file = Path(sys.argv[1])
    translate_file = Path(sys.argv[2])
    output_file = Path(sys.argv[3])

    # Baca source (xml/txt)
    source_text = source_file.read_text(encoding="utf-8")

    # Ambil isi tiap <entry>...</entry>
    entry_pattern = re.compile(r'(<entry[^>]*>)(.*?)(</entry>)', re.DOTALL)
    entries = entry_pattern.findall(source_text)

    # Baca file translate (per baris, hapus tanda kutip luar)
    translations = []
    for line in translate_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('"') and line.endswith('"'):
            line = line[1:-1]  # hapus tanda " di awal/akhir
        translations.append(line)

    if len(entries) != len(translations):
        print(f"WARNING: Jumlah entry ({len(entries)}) != jumlah translate ({len(translations)})")
        print("Baris terakhir mungkin tidak sinkron.")

    # Replace isi tiap entry
    new_text = source_text
    for i, (start_tag, old_content, end_tag) in enumerate(entries):
        if i < len(translations):
            replacement = start_tag + translations[i] + end_tag
            # ganti hanya sekali (agar tidak replace semua kemunculan)
            new_text = new_text.replace(start_tag + old_content + end_tag, replacement, 1)

    # Simpan ke file baru
    output_file.write_text(new_text, encoding="utf-8")
    print(f"✅ Replace selesai. Hasil disimpan di: {output_file}")

if __name__ == "__main__":
    main()
