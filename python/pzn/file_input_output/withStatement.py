# saat membaca atau menulis file kita harus hati2
# karena kalo terjadi error dan lupa pake close(), bisa terjadi memory leak
# meskipun kita udha ga pake file tsb

# memastikan file pasti ditutup meskipun file error
# jadi kita gaperlu pake close() lagi karena with akan otomatis close

with open("nilai_siswa.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        print(f"{data[0]} : {data[1]}")
