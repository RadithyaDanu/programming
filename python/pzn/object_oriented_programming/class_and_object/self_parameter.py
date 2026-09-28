# parameter self itu sangat penting
# self adalah parameter khusus yg merujuk pada instance atau object yang sedang manggil methodnya
# jadi yang tadi mahasiswa1 kita panggil perkenalan, maka self tersebut adalah mahasiswa1
# kalo manggil mahasiswa2.perkenalan() maka yg di dalam selfnya adalah mahasiswa2
# dia tergantung object yang memanggil

# method dengan parameter
# paramter tidak hanya self, kita bisa nambahin parameter lain seperti function biasanya
# tapi di parameter pertama harus tambahin self
# semua yg bisa dilakuin di function, bisa dilakukan di method

class Mahasiswa():
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"halo nama sy {self.nama}")

    def halo(self, nama):
        print(f"halo {nama}, nama saya {self.nama}")


mahasiswa1 = Mahasiswa()
mahasiswa1.nama = "Radithya Danutirta"
mahasiswa1.perkenalan()
mahasiswa1.halo("radit")
