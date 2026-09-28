# methods adalah function di dalam class dan bisa dipanggil oleh object
# method = function yang menempel di class dan object

class Mahasiswa():
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"halo semua, nama saya {self.nama}")


mahasiswa = Mahasiswa()
mahasiswa.nama = "radithya danutirta"
mahasiswa.perkenalan()
