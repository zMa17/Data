import csv

# Baca CSV hasil translate
with open("EN_Caravan_translated.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=';')
    translated_entries = {row["name"]: row["translated_text"] or row["original_text"] for row in reader}

# Baca file XML asli
with open("EN_Caravan.xml", "r", encoding="utf-8") as f:
    xml_data = f.read()

# Replace isi entry dengan translate
import re
def replacer(match):
    name, text = match.group(1), match.group(2)
    return f'<entry name="{name}">{translated_entries.get(name, text)}</entry>'

new_xml = re.sub(r'<entry name="(.*?)">(.*?)</entry>', replacer, xml_data, flags=re.DOTALL)

# Simpan hasil
with open("EN_Caravan_translated.xml", "w", encoding="utf-8") as f:
    f.write(new_xml)

print("✅ Merge selesai! Cek file EN_Caravan_translated.xml")
