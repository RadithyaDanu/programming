# mendefinisikan ulang method parent di child class dgn immplementasi yg berbeda
# saat lakuin method ini, kalo kita mau manggil method parentnya, kita perlu manfaatin super()
# saat kita definisiin ulang method dari parent itu namanya overriding

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


class Motor(Kendaraan):
    def klakson(self):
        print(f"motor {self.info()} gapunya klakson")

    @override
    def nyalakan(self):
        print(f"motor {self.merk} dinyalakan otomatis")


motor = Motor("zx25r", 2026)
motor.nyalakan()
