import csv
import re
import os

# Minta nama file XML dari user
xml_file = input("Masukkan nama file XML (contoh: EN_Belltown.xml): ").strip()

# Pastikan file ada
if not os.path.exists(xml_file):
    print(f"❌ File {xml_file} tidak ditemukan!")
    exit()

# Baca isi file XML
with open(xml_file, "r", encoding="utf-8") as f:
    data = f.read()

# Cari <entry ...>...</entry>
entries = re.findall(r'<entry name="(.*?)">(.*?)</entry>', data, re.DOTALL)

# Tentukan nama file CSV (ganti ekstensi jadi .csv)
csv_file = os.path.splitext(xml_file)[0] + ".csv"

# Tulis ke CSV
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["name", "original_text", "translated_text"])
    for name, text in entries:
        writer.writerow([name, text, ""])

print(f"✅ Extract selesai! Cek file {csv_file}")
