import csv
from pathlib import Path

input_file = Path("data/raw/nilai_siswa.csv")
output_dir = Path("data/processed")
output_file = output_dir / "report_nilai.csv"

output_dir.mkdir(parents=True, exist_ok=True)

total = 0
count = 0

with input_file.open() as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += int(row["nilai"])
        count += 1

rata_rata = total / count

with output_file.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["metrik", "nilai"])
    writer.writerow(["rata_rata_nilai", rata_rata])

print("Report generated:", output_file)
