data = []


def tambah_pengeluaran():
    barang = input("masukkan pengeluaran :")
    harga = int(input("masukkan harga :"))
    data.append({"barang": barang,
                 "harga": harga})


def lihat_pengeluaran():
    print("Fungsi untuk melihat pengeluaran")
    for i in range(len(data)):
        print(f"{i+1}. {data[i]['barang']} - Rp{data[i]['harga']}")


def total_pengeluaran():
    tambah = 0
    for i in range(len(data)):
        tambah += data[i]['harga']

    print(tambah)


def keluar():
    print("Fungsi untuk keluar dari aplikasi")


def exit():
    print("Terima kasih telah menggunakan aplikasi ini")
    raise SystemExit


def main():
    while True:
        print("1. Tambah Pengeluaran")
        print("2. Lihat Pengeluaran")
        print("3. total Pengeluaran")
        print("4. Keluar")
        try:
            user = input("pilih menu:")
            if user == "1":
                tambah_pengeluaran()
            elif user == "2":
                lihat_pengeluaran()
            elif user == "3":
                total_pengeluaran()
            elif user == "4":
                print("Terima kasih telah menggunakan aplikasi ini")
                break
            else:
                print("Menu tidak tersedia")
                main()
        except ValueError:
            print("Input tidak valid")
            main()


main()
