
from dbfread import DBF
from pathlib import Path

# Locate the dataset
project_dir = Path(__file__).resolve().parent.parent

dbf_path = (
    project_dir
    / "data"
    / "S_USA.Fire_FPA_FOD_7th_Fires"
    / "S_USA.Fire_FPA_FOD_7th_Fires.dbf"
)

# Open the DBF file without loading all records into memory
table = DBF(str(dbf_path), load=False, encoding="utf-8", char_decode_errors="replace")
# Display dataset information
print("Total records:", len(table))

print("\nAvailable columns:")
for field in table.fields:
    print(f"{field.name} ({field.type})")

# Display five example records
print("\nFirst 5 records:")

for index, record in enumerate(table):
    print(f"\nRecord {index + 1}:")
    print(dict(record))

    if index == 4:
        break

from collections import Counter

years = Counter()

for record in table:
    years[record["FIRE_YEAR"]] += 1

print("\nRecords by year:")

for year, count in sorted(years.items()):
    print(f"{year}: {count}")
