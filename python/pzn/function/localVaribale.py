# kalo kita buat variabel di dalam function, variablenya bakal bersifat lokal
# gabisa dipake diluar function
def fungsi():
    x = 10
    print("nnilai x dalam fungsi", x)


fungsi()  # bakal cetak nilai x
fungsi(x)  # x merupakan variabel lokal yg hanya dideklarasikan di dalam function
# gabakal bisa jalan krn variabel x itu bersifat lokal. harus decclare  variabel global x
