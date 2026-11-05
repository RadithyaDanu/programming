import numpy as np
import pandas as pd

df = pd.read_csv('dirty_products_dataset_en.csv')
print(df.head())
print("========================")
print(df.describe())
print("========================")
print(df.info())
print("========================")
print(df.isnull().sum())
print("========================")
print(df.duplicated().sum())


# bikin rentang interquartile range dulu, bikin iqr 1 dan 3, lalu untuk titik iqr pake perhitungan
# iqr3 - iqr1
# nilai maksimum dan minimum(rentang) yang diterima/toleransi adalah nilai iqr x 1.5
q25, q75 = np.percentile(data, 25), np.percentile(data, 75)
iqr = q75 - q25
cut_off = iqr * 1.5
minimum, maximum = q25 - cut_off, q75 + cut_off

outliers = [x for x in data if x < minimum or x > maximum]

# ==============================================================================
# PENJELASAN METODE IQR (INTERQUARTILE RANGE) UNTUK DETEKSI OUTLIER
# ==============================================================================
#
# 1. CONTOH DATA (11 angka yang sudah diurutkan):
#    Data = [10, 15, 20, 22, 25, 28, 30, 32, 35, 40, 90]
#
# 2. HITUNG KUARTIL (Q1 & Q3):
#    - q25 (Q1) = 20  --> Nilai pembatas 25% data terendah.
#    - q75 (Q3) = 35  --> Nilai pembatas 75% data (atau 25% data tertinggi).
#
# 3. HITUNG IQR (Jarak antara Q1 dan Q3):
#    - iqr = q75 - q25
#    - iqr = 35 - 20 = 15
#    (IQR melambangkan sebaran 50% data yang berada di tengah).
#
# 4. HITUNG CUT-OFF (Batas Toleransi Outlier):
#    - cut_off = iqr * 1.5
#    - cut_off = 15 * 1.5 = 22.5
#    (Angka 1.5 adalah standar statistik untuk memberi jarak toleransi).
#
# 5. HITUNG BATAS MINIMUM & MAKSIMUM WAJAR:
#    - minimum = q25 - cut_off  = 20 - 22.5 = -2.5
#    - maximum = q75 + cut_off  = 35 + 22.5 = 57.5
#
# 6. KESIMPULAN DETEKSI:
#    - Rentang data wajar ada di antara -2.5 sampai 57.5.
#    - Angka 10 sampai 40 masuk dalam rentang wajar.
#    - Angka 90 berada di atas 57.5 (maximum), sehingga terdeteksi sebagai OUTLIER.
# ==============================================================================
