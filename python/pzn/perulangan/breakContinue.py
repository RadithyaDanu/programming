# break digunakan untuk menghentikan perulangan
# continue digunakan untuk menghentikan perulangan saat ini dan melanjutkan ke
# perulangan berikutnya

# break

angka = 7
while True:  # while true akan membuat perulangan tanpa henti, break digunakan untuk stop
    tebakan = int(input("tebak angka :"))
    if tebakan == angka:
        print("selamat tebakan anda benar")
        break
    else:
        print("tebakan anda salah, coba lagi")

# continue
# misal pengen cetak angka ganjil aja
for i in range(20):
    if i % 2 == 0:
        continue
    print(i)
