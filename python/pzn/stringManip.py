# gabungin string bisa pake tambah
# string gabisa ditambahin sama int, float, atau boolean
# maka dar itu harus ada pengubahan format input ke string pake str()

umur = 20
# nama = "nama saya radit, umur saya " + umur + "tinggal di bogor" #ini akan error
nama = "nama saya radit,  umur saya : " + str(umur) + " tinggal di bogor"
print(nama)

# panjang string
# untuk menghitun panjang string(per karakter pada string) bisa pake len()
# len() akan menghitung semua karakter termasuk spasi, simbol, dan angka
print(len(nama))

# akses karakter dalam string (indexing)
# tiap karakter punya posisi index yg dimulai dari 0
# kalo mau ambil karakter terakhir bisa pake index -1
print(f"index ke 0 : {nama[0]}")  # n

# string slicing
# mengambil sebagian karakter dari string, bisa pake slicing
# format slicing : string[start:end:step]
# kalo start dikosongin, maka default start = 0
# kalo end dikosongin, maka default end = -1 /index terakhir

print(f"substring dari index 0-10 : {nama[0:10]}")  # nama saya
print(f"substring dari index 10-20 : {nama[10:20]}")  # radit,  umur saya : 20
print(f"substring dari index -10:-1 : {nama[-10:-1]}")  # tinggal di bogor
print(f"substring index 3-terakhir : {nama[3:]}")
# nmsy adt,umrsy:2tig i o
print(f"substring index 0-akhir step 2 : {nama[0::2]}")
# rogoB i g algit 02 : ayms rum ,tidar ,ayas am an
print(f"print semua string dari belakang : {nama[::-1]}")

# upper, lower, capitalize, title, strip, replace, split, join, count
# upper() = mengubah semua karakter menjadi huruf besar
# lower() = mengubah semua karakter menjadi huruf kecil
# capitalize() = mengubah karakter pertama menjadi huruf besar
# title() = mengubah karakter pertama dari setiap kata menjadi huruf besar
# strip() = menghapus spasi di awal dan akhir string
# replace() = mengganti karakter tertentu dengan karakter lain
nama = nama.replace("radit", "danu")
print(nama)
# split() = memisahkan string menjadi list berdasarkan karakter tertentu
# join() = menggabungkan list menjadi string berdasarkan karakter tertentu
# count() = menghitung jumlah kemunculan karakter tertentu dalam string
# find() = mencari posisi karakter tertentu dalam string, jika tidak ditemukan akan mengembalikan -1

# karakter khusus dalam string
# newline = "\n"  # membuat baris baru
# tab = "\t"  # membuat tabulasi
# \ backslash
print("halo \n selamat datang \t \"di\" python \\semoga bermanfaat")
