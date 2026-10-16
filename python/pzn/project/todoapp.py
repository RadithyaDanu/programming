task = []


def tambah_tugas():
    user_input = input("Masukkan tugas : ")
    task.append({"nama": user_input, "selesai": False})

    print("tugas berhasil ditambahkan!")


def lihat_tugas():
    for i, items in enumerate(task):
        status = "selesai" if items['selesai'] else 'belum selesai'
        print(f"{i + 1}. {items['nama']} - {status}")


def tugas_selesai():

    data = [i+1 for i in range(len(task))]

    print("daftar tugas")
    for i, items in enumerate(task):
        print(f"{i + 1}. {items['nama']} - {items['selesai']}")

    try:
        user_input = int(input("masukkan tugas yang ingin diselesaikan : "))
        if user_input not in data:
            print("data tidak ada")

    except ValueError:
        print("input yang benar woi")

    for i in range(len(task)):
        if i+1 == user_input:
            task[i]['selesai'] = True


def hapus_tugas():
    data = [i+1 for i in range(len(task))]
    try:
        user_input = int(input("masukkan tugas yang ingin diselesaikan : "))
        if user_input not in data:
            print("data tidak ada")
    except ValueError:
        print("input yang benar woi")

    index = user_input - 1
    hapus = task.pop(index)

    print(f"{hapus['nama']} tlah dihapus")
    print("data sekarang : ")
    for i, items in enumerate(task):
        print(f"{i+1}. {items['nama']} - {items['selesai']}")


def keluar():
    exit()


def main():
    print("=== TO DO LIST APP ===")
    print("1. tambah tugas")
    print("2. lihat tugas")
    print("3. tandai tugas selesai")
    print("4. hapus tugas")
    print("5. keluar")

    while True:
        try:
            user_input = int(input("pilih menu : "))
        except ValueError:
            print("mohon masukkan input yang sesuai")
            continue

        if user_input not in [1, 2, 3, 4, 5]:
            print("input tidak ada, coba lagi")
            continue

        if user_input == 1:
            tambah_tugas()

        if user_input == 2:
            lihat_tugas()

        if user_input == 3:
            tugas_selesai()

        if user_input == 4:
            hapus_tugas()

        if user_input == 5:
            keluar()


main()
