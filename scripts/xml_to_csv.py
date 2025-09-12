import csv
import re

# [UBAH SESUAI NAMA FILE XML] 
with open("EN_Coral.xml", "r", encoding="utf-8") as f:
    data = f.read()

entries = re.findall(r'<entry name="(.*?)">(.*?)</entry>', data, re.DOTALL)

# [UBAH SESUAI NAMA FILE CSV]
with open("EN_Coral.csv", "w", newline="", encoding="utf-8") as f:
    writer = writer = csv.writer(f, delimiter=";")
    writer.writerow(["name", "original_text", "translated_text"])
    for name, text in entries:
        writer.writerow([name, text, ""])

# [UBAH SESUIAI NAMA FILE CSV]
print("✅ Extract selesai! Cek file EN_Coral.csv")
