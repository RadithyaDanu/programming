# digunakan untuk menggabungkan beberapa kondisi logika, misalnya AND, OR, NOT
# and mengembalikan True jika kedua kondisi bernilai True, jika salah satu bernilai False maka hasilnya False
# or mengembalikan True jika salah satu kondisi bernilai True, jika kedua kondisi bernilai
# False maka hasilnya False
# not mengembalikan True jika kondisi bernilai False, jika kondisi bernilai True maka hasilnya False

# contoh
umur = 30
print(umur > 20 and umur < 40)  # True
print(umur < 20 or umur > 40)  # False

hari = "senin"
print(hari == "senin" or hari == "selasa")  # True

aktif = True
print(not aktif)  # False
