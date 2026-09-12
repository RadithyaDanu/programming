# argumen merupakan nilai yg kita kirim ke paramter functon
# saat manggil argumn, harus sesuai dengan posisi paramternya. gaboleh dibalik
# kalo kita pengen ubah posisi argumen itu bisa, kayak ga harus sesuai dengan posisi paramter
# harus disebutkan nama paramternya secar eksplisit
# keyword argument bisa di kombinasikan dengan argumen biasa

def argumen(nama, umur, kota="bogor"):
    print("nama", nama)
    print("umur", umur)
    print("kota", kota)


print("ini penulisan argumen biasa pada function")
argumen("radit", 20, "bogor")

print("ini penulisan keyword argumen pada function")
# urutan bebas
# sebutin paramternya lalu value
argumen(umur=25, nama="radit")

# bisa digabungkna dengan keyword biasa
