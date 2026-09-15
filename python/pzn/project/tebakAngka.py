def app_tebak_angka():
    import random

    angka_random = random.randint(1, 100)
    max_percobaan = 3
    percobaan = 0
    while percobaan < max_percobaan:
        try:
            tebakan = int(input("masukkan angka : "))
        except ValueError:
            print("masukkan input yang valid!")
            continue

        percobaan += 1

        if tebakan == angka_random:
            print("tebakanmu benar!")
            break
        elif tebakan > angka_random:
            print("angkamu terlalu besar!")
        elif tebakan < angka_random:
            print("angkamu terlalu kecil!")
    else:
        print("percobaan habis, kamu gagal!")
        print(f"angka sebenarnya adalah {angka_random}")


def app_menu():
    print("permainan tebak angka")
    print("1. tebak angka")
    print("2. keluar")

    pilihan = input("masukkan pilihan : ")

    if pilihan == "1":
        app_tebak_angka()
    elif pilihan == "2":
        print("selamat tinggal")
    else:
        print("pilihan tidak valid")


app_menu()
