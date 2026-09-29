# Tanpa constructor
class Mahasiswa:
    nim = 0
    nama = ""

    def setup(self, nim, nama):
        self.nim = nim
        self.nama = nama


mhs = Mahasiswa()
mhs.setup(1234, "radit")
# kalo gapake constructor harus panggil setupnya, jadi panggil class dan panggil setupnya
print(mhs.nim)
print(mhs.nama)

# Dengan constructor


class MahasiswaBaru:
    nim = 0
    nama = ""

    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


mhs_baru = MahasiswaBaru(1234, "radithya")
print(mhs_baru.nim)
print(mhs_baru.nama)

# __init__ adalah constructor pada class.
# Constructor otomatis dijalankan ketika object dibuat.
#
# Jadi kita tidak perlu membuat object terlebih dahulu
# lalu memanggil method setup() secara manual.
#
# Saat MahasiswaBaru(1234, "radithya") dipanggil,
# Python otomatis menjalankan __init__().
#
# self mengacu pada object yang baru saja dibuat.
# self.nim = nim -> menyimpan nim ke attribute object
# self.nama = nama -> menyimpan nama ke attribute object
