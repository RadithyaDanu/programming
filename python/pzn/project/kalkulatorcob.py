def penjumlahan(a, b):
    return a+b


def pengurangan(a, b):
    return a-b


def perkalian(a, b):
    return a*b


def pembagian(a, b):
    return a/b


def pangkat(a, b):
    return a**b


def modulus(a, b):
    return a % b


def keluar():
    exit()


def main():
    while True:
        print("kalkulator sederhana")
        print("1. penjumlahan")
        print("2. pengurangan")
        print("3. perkalian")
        print("4. pembagian")
        print("5. pangkat")
        print("6. modulus")
        print("7. keluar")
        try:
            user_milih = int(input("pilih menu : "))
        except ValueError:
            print("mohon masukan input yang valid")
        if user_milih not in [1, 2, 3, 4, 5, 6, 7]:
            print("gunakan angka valid!")
            continue

        try:
            angka1 = int(input("masukkan angka 1 = "))
            angka2 = int(input("masukkan angka 2 = "))

            if user_milih == 1:
                jumlah = penjumlahan(angka1, angka2)
                print(f"hasil penjumlahan {jumlah}")
            elif user_milih == 2:
                kurang = pengurangan(angka1, angka2)
                print(f"hasil pengurangan {kurang}")
            elif user_milih == 3:
                kali = perkalian(angka1, angka2)
                print(f"hasil perkalian {kali}")
            elif user_milih == 4:
                bagi = pembagian(angka1, angka2)
                print(f"hasil pembagian {bagi}")
            elif user_milih == 5:
                pangkt = pangkat(angka1, angka2)
                print(f"hasil pangkat {pangkt}")
            elif user_milih == 6:
                modul = modulus(angka1, angka2)
                print(f"hasil modulus{modul}")
            elif user_milih == 7:
                keluar()
            else:
                print("masukkan angka yang sesuai")

        except ValueError:
            print("mohon masukan input yang valid")
        except ZeroDivisionError:
            print("tidak bisa dibagi 0")


main()
