import random

angka_benar = random.randint(1, 100)
kesempatan = 0

print("=== NUMBER GUESSING GAME ===")
print("Tebak angka 1-100")
print("7x kesempatan")

while kesempatan < 7:
    try:
        tebakan = int(input("masukkan tebakan : "))
    except ValueError:
        print("mohon masukan input yang benar")
        continue

    kesempatan += 1
    if tebakan > angka_benar:
        print("terlalu besar!\n")
    elif tebakan < angka_benar:
        print("terlalu kecil!\n")
    else:
        print("BENAR! Kamu berhasil menebak angka!")
        print(f"jumlah percobaan : {kesempatan}")
        break

else:
    print(f"angka yang benar {angka_benar}")
    print(f"kamu gagal, percobaan : {kesempatan}")
