# operator khusus untuk bekerja dengan string
# contatenation = menggabungkan string =
# repetition = mengulang string
# membership = mengecek apakah string ada di dalam string lain

# contenation
nama_depan = "John"
nama_belakang = "Doe"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

# repetition
teks = "Hello, World! "
print(teks * 3)

# membership
teks = "Hello, World!"
print("Hello" in teks)  # True
print("Python" in teks)  # False
