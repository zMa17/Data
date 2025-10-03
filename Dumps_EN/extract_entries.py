#!/usr/bin/env python3
# extract_entries.py
# Usage:
#   python extract_entries.py path/to/file.xml
#   cat file.xml | python extract_entries.py

import re
import sys
from pathlib import Path

def extract_entries(text: str):
    # Ambil konten antara <entry ...> dan </entry>
    # DOTALL supaya menangkap newline juga
    pattern = re.compile(r'<entry[^>]*>(.*?)</entry>', re.DOTALL | re.IGNORECASE)
    matches = pattern.findall(text)
    # normalisasi whitespace baris jadi satu spasi, dan trim
    cleaned = [" ".join(m.split()).strip() for m in matches]
    return cleaned

def main():
    if len(sys.argv) > 1:
        p = Path(sys.argv[1])
        if not p.exists():
            print(f"File not found: {p}", file=sys.stderr)
            sys.exit(1)
        text = p.read_text(encoding='utf-8')
    else:
        text = sys.stdin.read()

    entries = extract_entries(text)
    if not entries:
        print("Tidak menemukan <entry>...</entry> apapun.", file=sys.stderr)
        sys.exit(1)

    for e in entries:
        print(f"\"{e}\"\n")  # cetak sesuai format yang kamu contohkan

if __name__ == "__main__":
    main()
