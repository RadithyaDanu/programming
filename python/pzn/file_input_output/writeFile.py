print("simpan data nilai")


file = open("nilai_siswa.txt", "w")

while True:
    nama = input("masukkan nama siswa = ")
    if nama == "":
        break

    nilai = input("masukkan nilai = ")

    # setelah itu tulis ke filenya

    file.write(f"{nama}, {nilai}\n")
    print(f"data {nama} behasil disimpan")

file.close()
print("semua data berhasil disimpan ke nilai_siswa.txt")
