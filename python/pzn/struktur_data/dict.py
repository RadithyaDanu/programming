# dictionary merupakan data dalam bentuk pasangan key dan value
# ditulis dalam kurung kurawal {}
# kalo di list, keynya adalah index, sedangkan dict ini keynya gaperlu pake index, bisa pake string, dll (bisa kita tentuin)
# wajib tentukan keynya
# tipe data key di dict bisa pake apa aja
# untuk aakses data dan ngubah value bisa pake key dengan [] sperti di list
# tapi di list pake index, disini pake keynya
# mau ngapus value di dict bisa pake kata kunci del
# panjang dict pake len()
# bisa diiterasi pake for

# dict siswa
siswa = {
    "nama": "radithya",
    "kelas": 9,
    "umur": 20,
    "asal": "bogor"
}

print(siswa)
print("dict siswa nama : ", siswa["nama"])
print("dict siswa kelas : ", siswa["kelas"])
print("dict siswa umur : ", siswa["umur"])

# nambah data pada dictionary
siswa["hobi"] = "nonton"
print(f"nambah hobi : {siswa}")

# mengubah nilai
siswa["kelas"] = 12
print("perubahan pada kelas dari 9 jadi 12 : ", siswa["kelas"])

# menghapus key-value
del siswa["kelas"]
print("hapus key dan value kelas di dict", siswa)

# iterasi
# iterasi ini ngambil keynya aja, sebenernya penamaan key diiterasi ini bisa bebas
# jatohnya kayak for i in siswa.....
# dan yg diambil cmn keynya aja
for key in siswa:
    print("iterasi dict siswa", key, ":", siswa[key])

# iterasi key-value pairs
# kalo pengen sekalian ambil key value, bisa begini
# tapi di dictnya harus pake function bernama items()
for key, value in siswa.items():
    print(key, "=", value)
