# penanganan error sangat penting agar program kita tidak crash tiba tiba saat dijalankan
# try except digunakan untuk menangani error yg mungkin terjadi
# kita pke try trs masukin kode yg mungkin error trs kasih except untuk kaloterjadi error

# contoh di kalkulator
try:
    angka1 = int(input("masukkan angka pertama : "))
    angka2 = int(input("masukkan angka kedua : "))
    hasil = angka1 + angka2
    print("hasil : ", hasil)
except:
    print("terjadi kesalahan!")

print("program selesai1")
# kesalahan pada kalkulator misal user input string seperti huruf pada program
# jd dibagian except itu diekskusi kalo kode dalam try itu terjadi error
# kalo ga pake try except, program akan langsung crash saat pertama kali melakukan kesalahan
# sedangkan jika pake try except, program akan mengeksekusi kode pada except terlebih dahulu, sehingga program tidak crash
# jadi program akan terus berjalan, namun error pada try akan diabaikan dan tidak membuat crash program
