# super() digunakan untuk mengaksees method atau atribute dari parent class
# super biasanya sering digunakkan untuk manggil constructor (__init__) di parentnya
# misal kita bikin constructor di childnya, dan pengen manggil constructor di parentnya
# karena namanya sama init, gimana caranya bisa manggil dari parent
# intinya method dari child class yg sama dengan method di parent class dan kita pengen
# manggil method dari si parentnya, harus pake super()
# misal di parent ada method info, terus kita juga pengen bikin method info di childnya
# nah setelah itu kita juga pengen manggil method info dari parent
# otomatis kita perlu super() untuk manggil method info dr parent tsb

# bikin parent
class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun

    def info(self):
        return f"{self.merk}, tahun {self.tahun}"

    def nyalakan(self):
        print(f"{self.merk} dinyalakan")

# child class/subclass


class Mobil(Kendaraan):
    def __init__(self, merk, tahun, jumlah_roda):
        super().__init__(merk, tahun)  # gaperlu pake self lagi
        self.jumlah_roda = jumlah_roda

    def klakson(self):
        print(f"mobil {self.info()} punya klakson")

    # def info(self):
    # nah kalo misal kita bikin methodinfo lagi, cara pemanggilan untuk info di parent class tuh gini
    # super().info(), kalo gapake super, yang dipangill method di childny


mobil_radit = Mobil("aston martin", 2026, 4)
print(mobil_radit.jumlah_roda)

# kita pengen bikin jumlah roda, berarti kita harus bikin init, nanti yg dipanggil di mobil
# kita jg pengen manggil dari parent, maka kita harus pake super
# kalo gapake super dan init doang, nanti method di mobil yg dipanggil bukan kendaraan
# ini cocok kalo sudah ada di parent dan mau dibuat ulang methodnya
# kalo childnya gaada ya gaperlu super
# super().__init__(merk, tahun)
# sebenarnya seperti memanggil:
# Kendaraan.__init__(self, merk, tahun)
