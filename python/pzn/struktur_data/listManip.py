# akses list sama kayak string, pake index dimulai dari 0
# misal variabel[0]

# mengubah elemen di list, bisa pake index, jadi misal vriabel[1] = masukkan nilai baru yang diinginkan

# mau nmabah elemen ke list, bisa pake method namanya append(data) untuk menambahakn data di paling akhir
# .append()

# misal mau nambahin data ditengah, pake insert(index, data).index disitu posisi yg diinginkan, data itu data yg pengen diinput

# hapus elemen bisa pake remove(index) atau pake pop() buat hapus elemn terakhir
# kalo hapus data, indexnya nanti bergeser, misal  hapus data index 0, maka data index 1 bakal jd index 0
# menghitung panjang list, bisa pake func len(list)
# list bisa digabung dengan list lain dengan operator tambah
# list juga bisa diiterasi dengan for loop

# akses elemen
buah = ['apel', 'jeruk', 'mangga', "semangka"]
print(buah[0])
print("aksesn elemen : ", buah[1])

# mengubah elemen di list
warna = ['merah', 'biru']
warna[0] = 'kuning'
print('ubah elemen : ', warna[0])

# nambah elemen
elektronik = ['hp', 'laptop']
elektronik.append('tv')
print("hasil penambahan tv : ", elektronik[2])

elektronik.insert(1, 'earphone')
print('hasil insert data di index yg diinginkan (1, earphone) : ',
      elektronik[1])

# remove
# yg diremove itu datanya bukan indexnya
buah.remove("jeruk")
print("hasil remove buah apel pada index 0 akan menjadi jeruk : ", buah)

buah.pop()
print("menghapus data pada index terakhir yaitu semangka, sisa apel dan mangga : ", buah)


del buah[0]
print("menghapus data sesuai index yg diinginkan : ", buah)

# mengecek panjang
print("panjang list elektronik adalah : ", len(elektronik))


# gabungin list
angka1 = [1, 2, 3, 4, 5]
angka2 = [6, 7, 8, 9, 10]
gabungan = angka1 + angka2
print("hasil gabungan list angka 1-5 dan 6-10 : ", gabungan)


# perulangan pada list
kendaraan = ["motor", "mobil", "pesawat", "kapal", "roket"]
for i in kendaraan:
    print("hasil dari loop pada list kendaraan : ", i)

# perulangan dengan mengakses index
# jadi disini mengakses index pertama sampai index ke 4 pada list kendaraan
# kalo di perulangan pertama kan dia langsung cetak aja
for i in range(0, len(kendaraan)):
    print(kendaraan[i])


# pengecekan
if "motor" in kendaraan:
    print("(((pengecekan))) ada motor")
