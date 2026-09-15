def app_tebak_angka():
    import random

    angka_random = random.randint(1, 100)


def app_menu():
    print("permainan tebak angka")
    print("1. tebak angka")
    print("2. keluar")

    pilihan = input("masukkan pilihan : ")

    if pilihan == "1":
        app_tebak_angka()
    elif pilihan == "2":
        print("selamat tinggal")
        break
    else:
        print("pilihan tidak valid")
