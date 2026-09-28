# membandingkan 2 buah object
# method __eq__() - utk bandingin
# bandingin object dengan object lain
# saa tkita pake operator perbandingan == maka method yg dipanggil equal itu

class Mahasiswa():
    nim = 0
    nama = ""

    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def __str__(self):
        return f"nim = {self.nim}, nama = {self.nama}"
        # returnya wajib string

    def __eq__(self, other):
        return self.nim == other.nim and self.nama == other.nama


mhs1 = Mahasiswa("1234", "radit")
mhs2 = Mahasiswa("1234", "radit")
print(mhs1 == mhs2)
