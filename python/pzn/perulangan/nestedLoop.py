# menempatkan perulangan di dalam perulangan
# for dalam for, while dalam while, while dalam for, for dalam while

print("tabel perkalian 1-5")
for i in range(1, 6):  # disini looping 1-5
    for j in range(1, 6):  # disini looping 1-5 juga
        hasil = i * j
        print(f"{i} x {j} = {hasil}")

# perulangan yang terjadi adalah, saat i melooping angka 1 lalu turun ke j
# maka j akan looping sebanyak 5x
# hasilnya = 1,1 ; 1,2 ; 1,3 ; 1,4 ; 1,5
# setelah loop di j habis, maka balik ke i lagi dengan mengambil 2 untuk di looping
