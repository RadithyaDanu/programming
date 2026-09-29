# bisa digunakan untuk pengecekan type
# bisa pake method/function isinstance(value, type) - untuk tipe object
# akan hasilin true kalo classnya adalah type tsb atau sub class dari type tsb
# jika bukan class/sub dgn type tsb maka hasolnya false

class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji


class KaryawanTetap(Karyawan):
    pass


class Manager(KaryawanTetap):
    pass


class VicePresident(Manager):
    pass


radit = Karyawan("radithya", 100000000)
danu = KaryawanTetap("danu", 2000000)
tirta = Manager("tirta", 30000000)
raditdanu = VicePresident("raditdanu", 40000000)

print(isinstance(radit, Karyawan))
print(isinstance(danu, Karyawan))
print(isinstance(tirta, Karyawan))
print(isinstance(raditdanu, Karyawan))
