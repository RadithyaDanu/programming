import pandas as pd

df = pd.read_csv("data.csv")


# 1. membuang kolom yang tidak diperlukan

# df = df.drop(columns=["No", "Legendary"])
# print(df)

# ini membuang kolom yang tidak diperlukan, kita manggil method drop() berisi columns yang kita
# ingin buang, sintaks seperti contoh. jadi langsgunt straight pake keyword argument berisi nama kolom

# 2.membuang missing value
# dropna = drop not available
# setelah manggil method dropna, kita pake keyword argument subset=[], yg berarti subset equal dengan
# list nama kolomnya
# df = df.dropna(subset=["Type2"])
# print(df.to_string())


# 3. mengisi missing value dengan default value
# disini kita butuh nama key dan value yang dibutuhkan jika data dalam kolom tersebut kosong
df = df.fillna({"Type2": "None"})
print(df.to_string())

# 4. fix inconsistent value
# mengubah kata yang acak2an menjadi lebih beraturan
# pilih kolomnya (series selecting), access kolom itu, panggil replace method dan
# masukin dict berisi value yang ingin diganti dan value hasil
df["Type1"] = df["Type1"].replace({"Grass": "GRASS"})
print(df)


# 5. standarisasi text
# mengubah teks menjadi seragam (besar semua atau kecil semua)
# declare nama kolom yg ingin diubah, panggil nama data series, access str, jadiin lower
df["Name"] = df["Name"].str.lower()
print(df)


# 6. fix data type
# mengubah tipe data
# panggil series df legendary, reasign sebagai value, panggil method astype, tentuin tipe yg dipengen
df["Legendary"] = df["Legendary"].astype(bool)
print(df)

# 7. duplicate values
# assign dataframe, reassign dataframe, panggil method drop_duplicates
# ini berlaku langsung ke dataframe, kalo pengen tertentu aja ya gt samain kek atas

df = df.drop_duplicates()
print(df.head())


# kenapa disini ada yang manggil kolom dalam argumen dan sebagai series di awal
# karena method yang dibuat itu punya tujuan tersendiri ke series atau df
# jadi ada method yang emang buat series dan juga ada yang buat df
# kalo pengen ngubah 1 kolom, pake series aja
# kalo pengen ngubah the whole dataframe, panggil nama kolom di argumen
