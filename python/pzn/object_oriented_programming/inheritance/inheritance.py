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


class Mobil(Kendaraan):  # disini konsep inheritance dari parent, otomatis semua di parent ada disini
    def klakson(self):
        print(f"mobil {self.info()} punya klakson")


mobil1 = Mobil("civic", 2020)
mobil1.nyalakan()
mobil1.klakson()


class Motor(Kendaraan):
    def klakson(self):
        print(f"motor {self.info()} gapunya klakson")


motor = Motor("zx", 2025)
motor.klakson()
motor.nyalakan()
