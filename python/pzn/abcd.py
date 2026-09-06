# variables
# biasa aja bikin nama, formatnya pake huruf kecil semua,
# kalo lebih dari satu kata pake underscore
# jangan pake spasi, simbol, keyword python, dan angka di awal nama variabel
nama = "John Doe"
umur = 30
tinggi = 175.5
is_student = True
# tipe data
# string = pake kutip/teks, int = bilangan bulat,
# float = bilangan desimal, boolean = True atau False

# Assignment
# merupakan proses pemberian nilai ke variabel, bisa pake tanda sama dengan (=)

# pengecekan tipe data
print("pengecekan tipe data nama, umur, tinggi, dan is_student")
print(type(nama))  # <class 'str'>
print(type(umur))  # <class 'int'>
print(type(tinggi))  # <class 'float'>
print(type(is_student))  # <class 'bool'>
x = [5, 'danu', 1+3j]
x[1] = 'radit'
print(x)


# input dan output dari user
# input() digunakan untuk mengambil input dari user, dan output bisa pake print()
masukinNama = input("masukin nama ")
# output
print("nama:", nama)
print("nama yang dimasukin adalah", masukinNama)
print(f"nama yang dimasukin adalah {masukinNama}")  # f-string
