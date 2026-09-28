# instance attribute hanya tersimpan di object hasil instansiasi dari class
# dan tidak akan ada di object manapun meskipun classnya sama

# jika ingin membuat attribut yang secara default ada di semua object hasil instansiasi
# kita perlu membuat class attribute, yaitu attribute yang didefinisikan dalam classnya

class Kampus:
    nama = ""
    alamat = ""


kampus = Kampus()
print(kampus.nama)
print(kampus.alamat)


class Mahasiswa():
    nim = 0
    nama = ""


mahasiswa = Mahasiswa()
print(mahasiswa.nim)
print(mahasiswa.nama)

# jika kita bikin class attribute, maka semua object yang instansiasi pada class tsb akan
# memiliki attribute default
# intinya tiap bikin object dr class, punya attribute default
