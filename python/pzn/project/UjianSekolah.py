# membaca soal dari file
# mengacak soal ujian
# mengacak posisi jawaban soal
# hasil score murid


# 1 membuka file soal
def ambil_soal():
    soalUjian = []
    with open("bankSoal.txt", "r") as file:
        for line in file:
            soalUjian.append(line.strip())
    return soalUjian


def buat_soal():
    soalUjian = ambil_soal()

    import random
    # acak soal
    random.shuffle(soalUjian)

    soal_asli = []

    for i in range(10):
        # formatnya akan pertanyaan|jawaban1, jawaban2, jawaban3, jawaban4
        soal = soalUjian[i]
        # ["pertanyaan", "jawaban1,jawaban2,jawaban3,jawaban4"]
        data = soal.split("|")

        pertanyaan = data[0]  # pertanyaan
        semua_jawaban = data[1]  # "jawaban1,jawaban2,jawaban3,jawaban4"

        # ["jawaban1","jawaban2","jawaban3","jawaban4"]
        jawaban = semua_jawaban.split(",")
        jawaban_benar = jawaban[0]  # jawaban1

        # acak jawaban
        # acak, bisa aja nanti gini ["jawaban2", "jawaban1", "jawaban4", "jawaban3"]
        random.shuffle(jawaban)

        soal_asli.append({
            "pertanyaan": pertanyaan,
            "semua_jawaban": jawaban,
            "jawaban_benar": jawaban_benar
        })

    return soal_asli


def app_ujian():
    soal_ujian = buat_soal()

    opsi = ["a", "b", "c", "d"]

    jawaban_betul = 0
    jawaban_salah = 0

    for i in range(len(soal_ujian)):
        soal = soal_ujian[i]
        print(f"pertanyaan {i + 1}. {soal['pertanyaan']}")
        print("jawaban")
        for j in range(len(soal["semua_jawaban"])):
            jawab = soal["semua_jawaban"][j]
            print(f"{opsi[j]}. {jawab}")

        try:
            jawaban = input("Masukkan jawaban (a/b/c/d) = ")
            jawaban_user_index = opsi.index(jawaban)
            jawaban_user_akhir = soal["semua_jawaban"][jawaban_user_index]

            if jawaban_user_akhir == soal["jawaban_benar"]:
                jawaban_betul += 1
            else:
                jawaban_salah += 1

        except ValueError:
            print("masukan input yg sesuai")
    print(f"jawaban benar = {jawaban_betul}")
    print(f"jawaban_salah = {jawaban_salah}")


app_ujian()
