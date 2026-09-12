# kalo kita buat variabel di dalam function, variablenya bakal bersifat lokal
# gabisa dipake diluar function
def fungsi():
    x = 10
    print("nnilai x dalam fungsi", x)


fungsi()  # bakal cetak nilai x
fungsi(x)
