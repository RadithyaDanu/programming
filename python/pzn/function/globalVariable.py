# variable yang dibuat diluar function
# bisa digunakan di dalam function

# kita gabisa ngubah/nilai dari global variabel di dalam funcction
# kalo mau ngubah wajib pake keyword global di dalam function

nama_global = "radit"


def tampilkan_nama():
    print("nama adalah : ", nama_global)  # bisa akses global variable


def ubah_nama():
    global nama_global
    nama_global = "danu"

# jika pada function ubah_nama() tidak pake global nama_global
# maka nama_global pada function tsb merupakan deklarasi variabel baru  di dala function tsb


tampilkan_nama()  # bakal cetak radit
ubah_nama()  # running function untuk ngubah value daria variabel global
tampilkan_nama()  # bakal cetak danu
