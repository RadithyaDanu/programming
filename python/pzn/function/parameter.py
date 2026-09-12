# parameter memungkinkan kita mengirim data ke function untuk diolah difunctionnya
# caranya nambahin nama didalam kurung buka tutup
# parameter >1 bisa pake koma sebagai pemisah
# jika kita isi parameter, maka kita wajib isi data parameternya atau yang disebut argumen
# parameter = kita berikan saat deklarasi pertama sebagai data yang akan diolah di dalam function
# argumen = kita berikan saat menggunakan function di kode

def halo(nama):  # ini merupakan contoh parameter (nama)
    print(f"halo {nama} selamat datang")
# kalo kita nambahin parameter, dan pengen manggil function halo, wajib kasih argumen


# ini merupakan argumen, jadi radit akan dimasukan ke dalam function untuk diolah
halo('radit')


def persegi(panjang, lebar):
    luas = panjang * lebar
    print(
        f"luas persegi panjang dengan panjang : {panjang} dan lebar : {lebar} adalah {luas}")


persegi(19, 2)
