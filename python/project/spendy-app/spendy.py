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


def tambah_pengeluaran():

    nama_pengeluaran = input("masukkan nama pengeluaran = ")
    nama_kategori = input("masukkan nama kategori = ")
    jumlah_uang = int(input("masukkan jumlah uang = "))

    pengeluaran_user.append({
        "pengeluaran": nama_pengeluaran,
        "kategori": nama_kategori,
        "jumlah_duit": jumlah_uang
    })
    return pengeluaran_user


def lihat_pengeluaran():
    pengeluaran_semua = pengeluaran_user
    for data in pengeluaran_semua:
        for key, value in data.items():
            print(f"{key} : {value}")
    print("=====================")


def app_menu():
    while True:
        print("selamat datang di pencatatan keuangan")
        print("silahkan pilih menu yang diinginkan")
        print("1. tambah pengeluaran")
        print("2. riwayat pengeluaran")
        print("3. keluar")

        user_input = int(input("masukkan pilihan = "))

        if user_input == 1:
            tambah_pengeluaran()
        elif user_input == 2:
            lihat_pengeluaran()
        elif user_input == 3:
            print("selamat tinggal!")
            break
        else:
            print("input tidak_valid!")


app_menu()
