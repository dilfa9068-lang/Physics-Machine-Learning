import csv
import numpy as np

# 1. Membuat dan menyimpan file CSV
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

with open('contoh.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("File CSV 'contoh.csv' berhasil dibuat!")

# 2. Membaca file CSV dengan NumPy
data_csv = np.genfromtxt('contoh.csv', delimiter=',')
print("Data dari file CSV:\n", data_csv)

