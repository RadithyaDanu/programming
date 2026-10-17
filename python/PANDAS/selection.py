import pandas as pd

df = pd.read_csv("data.csv", index_col="Name")


#  SELECT BY COLUMN
# ini milih kolom mana aja yang mau ditampilin
# # print(df['Name'].to_string()) # to_string() dipake kalo pengen nampilin semua data
# # kalo mau print multiple kolom, kita harus buat list dalam list
# print(df[["No", "Type1"]])


# # select by row
# # sama kayak series, df.loc[indexnya]
# # bisa jg pake column sebagai index, di declare df awal, tambahin index_col = "namakolomnya"
# # jd df.loc['namakol']
# # dalam call df menggunakan index_col itu, filter kolomm yg ditampilin = ["height", "weight"]
# print(df.loc["Bulbasaur", ["Height", "Weight"]])
# # pake iloc jg sama aja
# # tapi struktur iloc gini
# # df.iloc[0:11:2, 0:3] > startstopstep, lanjut 3 kolom awal yg ditampilin

# input user mencari nama pada dataframe

pokemon = input("masukkan nama pokemon : ")
try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} was not found")
