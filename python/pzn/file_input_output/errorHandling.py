# meskipun pake with, tapi jika ada error maka aplikasi akan tetap berhenti
# pake try-except
# misal jika file yg pengen kita baca gaada, maka akan terjadi error FileNotFound misal

try:
    with open("nilai_siswa.tt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(f"{data[0]} : {data[1]}")

except FileNotFoundError:
    print("file tidak ditemukan")

# outputnya file tidak ditemukan
