# else di try except hanya dijalankan kalo gaada error
# kalo kita mau lakuin sesuatu baik terjadi error maupun tidak terjadi error pake finally


try:
    a = int(input("masukkan angka : "))
    print("angka = ", a)
except ValueError:
    print("angka tidak valid")
finally:
    print("program selesai")

# finally akan selalu dijalanin baik ada error maupun gaada error
