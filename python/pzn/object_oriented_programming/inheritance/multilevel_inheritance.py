# class bisa inherit dari class yang sudah inherit (inheritance chain)
# gaada batasan untuk inheritance, tapi jangan kebanyakan nnti susah dibaca

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
