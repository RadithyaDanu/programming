# di bbrp bahasa, class gabisa lakuin inheritance lebih dari 1 class
# jadi 1 class punya 2 parent itu gabisa contoh java
# inherit lebih dari 1 bahaya, bisa terjadi diamond problem
# 1 child class bisa punya multiple parent

class BisaBerenang:
    def berenang(self):
        print("bisa berenang")

    def berenang1(self):
        return "bisa berenang"


class BisaLari:
    def lari(self):
        print("bisa lari")


class Atlit(BisaBerenang, BisaLari):
    def __init__(self, nama):
        self.nama = nama

    def turunan(self):
        print(f"{self.nama} {super().berenang1()}")


contoh = Atlit("radithya")
contoh.berenang()
contoh.lari()
contoh.turunan()
