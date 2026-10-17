import pandas as pd

# dataframe merupakan tabular data structure dengan rows dan column (2d)
# kayak di excel, spreadsheet
# misal kita bikin dict employee berisikan beberapa data

data = {
    "nama": ["radithya", "danutirta", "subaru"],
    "age": [21, 20, 19]
}
# terus data itu kita ubah ke dataframe
# declare variabel untuk nyimpen dataframenya

df = pd.DataFrame(data)
print(df)

# rows berisi index, dan column berisi nama kolom
# dalam kasus dict ini, key nama dan key age otomatis menjadi kolom dan value list menjadi isi data
# kita juga bisa ubah index polos(0,1,2) menjadi index yang kita mau
# df = pd.DataFrame(data, index=["a", "b", "c"]) kayak biasa aja, perubahan harus mengikuti jumlah index
# kita juga bisa mengakses salah satu data, kita bisa pake method loc[]
# loc[] ini menuju label/index yang dimiliki dari si data, indexnya yg dari dataframe itu ya

print(f"data index ke 0 : \n{df.loc[0]}")

# di colab/jupyter bisa langsung head() tapi kalo disini gabisa, karena head() doang
# itu berarti ngambil 5 baris pertama aja, sedangkan print itu nampilin output di terminal

# kita juga bisa ngambil berdsarkan int location, misal labelnya ygawallnya index udah dicustom
# nah kita tetep bisa manggil via itu, tapi pake method iloc[], sm aja querynya


# cara nambah kolom
# jadi cuma tinggal panggil dfnya terus buat kolom baru df[] dan isi value kolomnya []
df["job"] = ["ML Engineer", "Software Engineer", "AI engineer"]
print(df)

# add a new row
# cara mudahnya itu bikin new dataframe and concatenate it
# didalam data baru yg dibuat dalam dataframe itu, bisa nambahin new row semau kita
# kita nyimpen dictnya di dalam list
new_data = pd.DataFrame([
                        {"nama": "danu", "age": 18, "job": "engineer"}], index=['4'])

# setelah itu kita gabungin sama data awal kita, gabunginnya dalam concat() itu tambahin list
# jadi concat([]), karena kita mau nambahin data, nah data itu bersifat didalam list
# jadi tiap kita mau nambah, manipulasi, itu selalu pake list.
df = pd.concat([df, new_data])
print(df)
# nah kalo kita add new row, indexnya bakal ngulang lagi ke 0, jadi dia pake index di new dataframe
# custom aja, langsung di new_data  setelah list data pake koma masukin index.
