# method __str__() - string representation
# method __str__() menentukan bagaimana object ditampilkan sebagai string

class Mahasiswa():
    nim = 0
    nama = ""

    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def __str__(self):
        return f"nim = {self.nim}, nama = {self.nama}"
        # returnya wajib string


# kalo gapake __str__()
# dan kita cuma panggil
# <__main__.BankAcc object at 0x000002707B6C6A50>
mhs = Mahasiswa("231011401920", "radidthya danutirta")
print(mhs)
