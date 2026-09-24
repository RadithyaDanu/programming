# ## PHASE 1 - PLANNING
# Tentukan kebutuhan dan fitur aplikasi sebelum mulai coding.
# Fitur minimum:
# 1. Tambah Pengeluaran
#    User dapat memasukkan:
#    * Nama pengeluaran
#    * Kategori
#    * Jumlah uang
# 2. Lihat Pengeluaran
#    Menampilkan seluruh pengeluaran yang telah dicatat.
# 3. Hitung Total
#    Menghitung seluruh jumlah pengeluaran.
# 4. Hapus Pengeluaran
#    User dapat menghapus pengeluaran tertentu.
# 5. Keluar
#    Menghentikan aplikasi.

# Contoh menu:
# === PENCATAT PENGELUARAN ===
# 1. Tambah pengeluaran
# 2. Lihat pengeluaran
# 3. Total pengeluaran
# 4. Hapus pengeluaran
# 5. Keluar
# Pilih menu:

pengeluaran_user = []


class menu_utama:
    def __init__(self, nama: str, kategori: str, harga: int):
        self.nama = nama
        self.kategori = kategori
        self.harga = harga


class fitur(menu_utama):

    def tambah_pengeluaran(self):
        nama_pengeluaran = input("masukkan nama pengeluaran = ")
        kategori_pengeluaran = input("masukkan nama kategori = ")
        harga_pengeluaran = int(input("masukkan harga = "))

        pengeluaran_user.append({
            "nama": nama_pengeluaran,
            "kategori": kategori_pengeluaran,
            "harga": harga_pengeluaran
        })

    def lihat_pengeluaran(self):
        data_user = pengeluaran_user
        if not data_user:
            print("data belum ada")
            return

        for key, value in data.items():
            print(f"{key} : {value}")
        print("================")


def tambah_pengeluaran():
    try:
        nama_pengeluaran = input("masukkan nama pengeluaran = ")
        nama_kategori = input("masukkan nama kategori = ")
        jumlah_uang = int(input("masukkan jumlah uang = "))

        pengeluaran_user.append({
            "pengeluaran": nama_pengeluaran,
            "kategori": nama_kategori,
            "jumlah_duit": jumlah_uang
        })
    except ValueError:
        print("masukkan input yang sesuai!")


def lihat_pengeluaran():
    data_user = pengeluaran_user
    if not data_user:
        print("belum ada data!")
        return

    for data in data_user:
        for key, value in data.items():
            print(f"{key} : {value}")
    print("=====================")


def hitung_total():
    jumlah = 0
    # data = pengeluaran_user["jumlah_duit"] ((salah krn pengeluaran user itu list, gabisa akses kyk dict))
    # data = pengeluaran_user
    # for i in len(data["jumlah_duit"]):
    #     jumlah += data[i]["jumlah_duit"]

    # for i in range(len(data)):
    #     jumlah += data[i]["jumlah_duit"] #ada 2 cara, 1 indexing, 2 itu. ambil simpel

    for data in pengeluaran_user:
        jumlah += data["jumlah_duit"]
    # pengeluaran_user berisi list yang menyimpan value dict. data pada for in
    # akan membuat vaiabel sementara yang berisi datanya
    # pada kasus ini, berarti data adalah valuenya si pengeluaran_user itu list berisi dict

    print(f"total pengeluaran = {jumlah}")


def hapus_data():
    data = pengeluaran_user
    print("data tersimpan")
    for i in range(len(data)):
        hasil = f"{i + 1}. {data[i]['pengeluaran']}"
        print(hasil)
    try:
        user_input = int(input("masukkan data yang ingin dihapus = "))
        index = user_input - 1
        hapus = data.pop(index)

        print(f"{hapus['pengeluaran']} berhasil dihapus")
        print(f"data sekarang :")
        for i in range(len(data)):
            hasil = f"{i + 1}. {data[i]['pengeluaran']}"
            print(hasil)

    except ValueError:
        print("masukkan input yang sesuai!")
    except IndexError:
        print("data tidak ada!")

    # salah
    # for i in range(len(hasil)):
    #     splitting = hasil.split('.')
    #     data_hasil = int(splitting[i])
    #     user_input = input("masukkan data yang ingin dihapus : ")

    # if user_input == data_hasil:
    #     hapus = data[data_hasil]
    #     del data[data_hasil]
    #     print(f"data {hapus} telah dihapus!")


def app_menu():
    while True:
        print("selamat datang di pencatatan keuangan")
        print("silahkan pilih menu yang diinginkan")
        print("1. tambah pengeluaran")
        print("2. riwayat pengeluaran")
        print("3. hitung total keseluruhan pengeluaran")
        print("4. hapus data")
        print("5. keluar")
        try:
            user_input = int(input("masukkan pilihan = "))

            if user_input == 1:
                tambah_pengeluaran()
            elif user_input == 2:
                lihat_pengeluaran()
            elif user_input == 3:
                hitung_total()
            elif user_input == 4:
                hapus_data()
            elif user_input == 5:
                print("selamat tinggal!")
                break
            else:
                print("input tidak_valid!")
        except ValueError:
            print("masukkan input yang sesuai!")


app_menu()
