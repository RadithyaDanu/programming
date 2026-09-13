# try except juga punya bagian else kayak if dan for
# bagian else ini dijalankan kalo ga terjadi error pada yang terjadi dalam try except
# kalo terjadi error bagian  ini ga dijalanin

try:
    a = int(input("masukkan angka : "))
except ValueError:
    print("masukkan angka yang valid")
else:
    print("angka yang anda masukkan = ", a)
    if a > 0:
        print("angka positif")
    elif a < 0:
        print("angka negatif")
    else:
        print("angka 0")
