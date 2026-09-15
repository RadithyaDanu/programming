# loop bisa pake else
# else dieksekusi jika  loop selesai secara normal (tidak dgn break)

kata = input("masukkan kata : ")
huruf_cari = input("masukkan huruf : ")

for huruf in kata:
    if huruf == huruf_cari:
        print(f"huruf {huruf_cari} terdapat di dalam kata {kata}")
        break
else:
    print(f"huruf {huruf_cari} tidak ditemukan dalam kata {kata}")
