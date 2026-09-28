# methods adalah function di dalam class dan bisa dipanggil oleh object
# method = function yang menempel di class dan object

class Mahasiswa():
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"halo semua, nama saya {self.nama}")

    # def perkenalan(mahasiswa):
        # print(f"halo nama saya {mahasiswa.nama}")

    # perkenalan(mahasiswa1)
    # ini function biasa, kita pengen perkenalan nempel di class/object dari mahasiswa

# bedanya antara bikin function dan method, kalo method selalu pake parameter self
# self itu referensi ke object saat ini.
# misal mau manggil nama object saat ini, kita pake self
# jadi manggilnya self.nama
# semua attribute class dipanggil dengan self.nama


mahasiswa = Mahasiswa()
mahasiswa.nama = "radithya danutirta"
mahasiswa.perkenalan()
# selfnya otomatis masukin variabel mahasiswa ke dalam method/self di perkenalan saat dipanggil
