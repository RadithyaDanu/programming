# saat kita nambahin parameter di function kita wajib isi nilai di parameter tsb
# tapi kita jg bisa nambahin yg namanya default parameter
# default parameter merupakan nilai awal dari paramter tsb
# menyebabkan kalo kita ngisi nilai pd parameter itu ga wajib lagi krn sudah ada defaut nilainya
# syaratnya : posisi default paramter gabisa didepan, harus dibelakang

# buat bikinnya cukup tambahin = lalu diikutin nilai defaultnya


def sapa_nama(nama, sapaan="halo"):
    print(sapaan, nama)

# artinya kalo kita manggil function ini, kita ga wajib buat ngisi argumen untuk parameter sapaan
# kita juga bisa ngisi parameter sapaan dengan kata yang kita mau


print("ini pemanggilan function tanpa mengisi default paramter akan hasilin halo sesuai default nilainya")
sapa_nama("radit")

print("ini pemanggilan function dengan ")
sapa_nama("danu", "hi")
