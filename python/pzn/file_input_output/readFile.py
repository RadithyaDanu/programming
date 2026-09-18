# untuk baca file kita pakai fungsi read(), ini akan mengembalikan seluruh isi file
# tapi kalo kita langsung read gitu aja dan filenya besar, maka akan bebanin memori kita
# cara lebih mudah agar penggunaan memori lebih efisien
# yaitu baca per baris
# dengan cara menggunakan iterasi for untuk membaca per baris

print("membaca file")

file = open("nilai_siswa.txt", "r")

for line in file:
    data = line.strip().split(",")
    print(f"{data[0]} : {data[1]}")

# strip() digunakan untuk emnghilangkan spasi di kanan atau kiri
# split(",") digunakan untuk membuat tampilan seperti list, dipisahkan dengan koma
file.close()
print("cetak selesai")
