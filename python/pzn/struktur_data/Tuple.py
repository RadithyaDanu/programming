# mirip seperti list tapi tidak bisa diubah setelah dibuat, sudah buat tuple dengan data tertentu, maka gabisa dihapus tambah edit dll
# tuple ditulis dengan kurung biasa ()
# buatnya juga langsung aja dan dipisah dengan koma, jummlah data bebas
# akses data dituple sama kayak list tuple[0]
# tuple gabisa diubah, jd gaada operasi untuk manipulasi data tuple
# panjang tuple pake len()

poin = (5, 10)
print(poin)
print("data tuple index ke 0 : ", poin[0])


tanggal_lahir = (14, "september", 2005)
print(tanggal_lahir)
# tuple digunakan untuk data tetap yang tidak diubah

# iterasi di tuple
for i in tanggal_lahir:
    print(i)

# iterasi di tuple dengan index
for i in range(0, len(tanggal_lahir)):
    print("loop dengan index pada tuple : ", tanggal_lahir[i])
