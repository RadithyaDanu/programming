import pandas as pd

# series
# adalah pandas 1 dimmensional label array, ini tuh kayak data 1 kolom di spreadsheet
# Series adalah constructor

data = [100, 102, 104]

series = pd.Series(data, index=['a', 'b', 'c'])
print(series)

print("==================")
temperature = [21, 22, 23]
hari: list[str] = ["senin", "selasa", "rabu"]
data_baru = pd.Series(temperature, index=hari, name="nyobain")
print(data_baru)
print("=====================")

# nah data itu bakal diubah jd 1 dimensional array, ada index dan value
# dibawahnya adalah metadata dari series ini, datatypenya int64
# metadata enyesuaikan value dari data yang diubah ke series
# kita juga bisa nambahin argumen dari constructornya, misalnya tambahin index
# nah index ini bisa berisi tipe data apapun, bahkan series lagi

# lalu ada properti location(loc)
# digunakan untuk mencari label pada suatu series
print(f"ini data dari label a : {series.loc['a']}")
# kayak nyari index aja sih tapi ini berbentuk series/data 1d

# ngubah data dari series
# ini sama aja kayak ngubah di list
series.loc['a'] = 200
print(f"hasil perubahan series a : {series.loc['a']}")

# kita jg bisa akses via index/int posisi (iloc)
print(f"ini adalah penggunaan properti iloc index 0 : {series.iloc[0]}")

# filter data
print(f"data kurang dari 200 : {series[series < 200]}")
