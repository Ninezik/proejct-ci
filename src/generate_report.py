from pathlib import Path
import pandas as pd

# pastikan folder ada
output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

# contoh isi report
df = pd.DataFrame({
    "nama": ["Ani", "Budi"],
    "nilai": [80, 90]
})

output_file = output_dir / "report_nilai.csv"
df.to_csv(output_file, index=False)

print(f"Report berhasil dibuat: {output_file}")
