from pathlib import Path
import pandas as pd

# path input & output
input_file = Path("data/raw/nilai_siswa.csv")
output_dir = Path("data/processed")
output_file = output_dir / "report_nilai.csv"

# pastikan folder processed ada
output_dir.mkdir(parents=True, exist_ok=True)

# baca data
df = pd.read_csv(input_file)

# (opsional) validasi sederhana
if df.empty:
    raise ValueError("Data kosong!")

# simpan report
df.to_csv(output_file, index=False)

print("Report berhasil dibuat")
print(f"Input : {input_file}")
print(f"Output: {output_file}")
