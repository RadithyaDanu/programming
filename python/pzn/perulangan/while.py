# mengulangi kode menggunakan kondisi
# selagi kondisi bernilai true makan perulangan akan selalu dijalankan
# jika kondisi bernilai false maka perulangan akan berhenti

angka = 1
while angka <= 5:
    print(f"angka ke {angka}")
    angka += 1


password = (f"masukkan password : ")
kesempatan = 0

while password != 12345:
    password = int(input("masukkan password :"))
    if password == 12345:
        print("password benar")
        break
    kesempatan += 1
    print(f"password salah, kesempatan ke {kesempatan}")
    if kesempatan == 3:
        print("kesempatan habis")
        break
