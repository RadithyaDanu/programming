# tujuan : aplikasi kalkulator sederhana
# kebuthan : operasi matemtatika sederhana, input output user, perulangan untuk input


def penjumlahan(a, b):
    return a + b


def pengurangan(a, b):
    return a - b


def pembagian(a, b):
    return a/b


def perkalian(a, b):
    return a * b


def pangkat(a, b):
    return a ** b


while True:
    print("1. penjumlahan")
    print("2. pengurangan")
    print("3. pembagian")
    print("4. perkalian")
    print("5. pangkat")
    print("6. keluar")

    user = input(f"masukkan operasi yang kamu inginkan (1-6): ")
    if user == "6":
        print("terimakasih telah mnggunakan aplikasi ini")
        break

    if user not in ["1", "2", "3", "4", "5", "6"]:
        print("mohon gunakan angka yang valid!")
        continue
    try:
        angka1 = int(input("angka pertama = "))
        angka2 = int(input("angka kedua = "))

        if user == "1":
            tambah = penjumlahan(angka1, angka2)
            print(f"{angka1} + {angka2} = {tambah}")

        elif user == "2":
            kurang = pengurangan(angka1, angka2)
            print(f"{angka1} - {angka2} = {kurang}")

        elif user == "3":
            bagi = pembagian(angka1, angka2)
            print(f"{angka1} / {angka2} = {bagi}")

        elif user == "4":
            bagi = perkalian(angka1, angka2)
            print(f"{angka1} x {angka2} = {bagi}")

    except ValueError:
        print("mohon gunakan angka yang valid!")

    lanjut = input("apakah mau lanjut? y/n = ")
    if lanjut.lower() == "n":
        print("terimakasih")
        break
