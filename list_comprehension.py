# list comprehension
# struktur list comprehension :
# [expression for item in iterable if condition]
# for list biasa gini:
angka = []

for i in range(10):
    angka.append(i)

print(angka)

# tapi kalo dijadiin list comprehension jadi gini:
# angka = [i for i in range(10)]
# cara bacanya dari kanan baru kiri
# jadi for i  in range(10) "untuk setiap i dari 0-9"
# i "masukkan i ke dalam list"
# jadi buat list yang berisi i dari range(10)

# struktu dasar [expression for item in iterable]
# kuadrat = [i ** 2 for i in range(5)]
# kalo ditulis biasa
kuadrat = []

for i in range(5):
    kuadrat.append(i ** 2)

# ini struktur penggunaan if [expression for item in iterable if condition]
# angka_genap = [i for i in range(10) if i % 2 == 0]
if_list = []
for i in range(10):
    if i % 2 == 0:
        if_list.append(i)


# penggunaan else [hasil_if if kondisi else hasil_else for item in iterable]
# hasil = ["genap" if i % 2 == 0 else "ganjil" for i in range(5)]

# nested loop hasil = [j for i in range(3) for j in range(3)]
hasil = []

for i in range(3):
    for j in range(3):
        hasil.append(j)

# nested list comprehension (membuat list dalam list)
hasil = [[j for j in range(3)] for i in range(3)]
hasil = []

for i in range(3):
    row = []

    for j in range(3):
        row.append(j)

    hasil.append(row)
