# try_except.py itu error handling general, apapun yang terjadi bakal masuk ke exceptnya
# kita bisa nentuin tipe errornya setelah kata kunci except
# sehingga jika terjadi error tipe/jenis tersebut, maka except tsb yg akan nanganin errornya
# kita bisa nambah lebih dari 1 except dalam blok try except

# misal disini kita bikin program kalkulator dengan except value error dan zero division error
try:
    angka1 = int(input("masukkan angka pertama : "))
    angka2 = int(input("masukkan angka kedua : "))
    hasil = angka1 / angka2
    print("hasil = ", hasil)
except ValueError:
    print("masukkan angka yang valid!")
except ZeroDivisionError:
    print("tidak bisa dibagi dengan 0!")
except:
    print("terjadi kesalahan lain!")
