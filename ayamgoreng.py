import pandas as pd

# 1. Baca CSV dan hapus spasi awal/akhir pada data & header
df = pd.read_csv(r'C:\fadil kodingan\Data Radiosonde\2026100200-08536 Lisboa portugal tanggal 2 oktober.csv', skipinitialspace=True)
df.columns = df.columns.str.strip()

# 2. Standarkan nama kolom (ubah spasi menjadi '_' dan hapus simbol '%')
df.columns = (
    df.columns.str.lower()
    .str.replace('%', 'pct')
    .str.replace(' ', '_')
)

# 3. Konversi kolom 'time' ke format Datetime
df['time'] = pd.to_datetime(df['time'])

# 4. Tangani duplikasi timestamp (ambil data baris terakhir atau rata-rata per detik)
df = df.drop_duplicates(subset=['time'], keep='last').reset_index(drop=True)

# 5. Opsional: Restriksi/Clip kelembaban (jika batas maksimum analisis adalah 100%)
# df['humidity_wrt_ice_pct'] = df['humidity_wrt_ice_pct'].clip(upper=100)

# 6. Simpan data yang sudah bersih ke file CSV baru
df.to_csv('cleaned_2026111000-08536.csv', index=False)
print("Pembersihan data selesai! Disimpan ke 'cleaned_2026111000-08536.csv'")