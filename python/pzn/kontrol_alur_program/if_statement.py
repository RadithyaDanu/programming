# dijalankan jika suatu kondisi bernilai True, jika bernilai False maka tidak dijalankan
# setelah if ada : dan indentasi (spasi) untuk menandai blok kode yang akan dijalankan jika kondisi true

angka = int(input("masukkan angka : "))
if angka > 0:
    print(f"angka {angka} adalah bilangan positif")
if angka < 0:
    print(f"angka {angka} adalah bilangan negatif")
if angka == 0:
    print(f"angka {angka} adalah nol")

# else dijalankan jika kondisi if bernilai False

nilai = 80
if nilai > 60:
    print(f"grade anda {nilai} . Anda lulus")
else:
    print(f"grade anda {nilai}. Anda tidak lulus")

# elif (else if). digunakan untuk mengecek beberapa kondisi secara berurutan. kalo if doang kan
# cuma 1 kondisi

grade = 85
if grade >= 90:
    print(f"grade anda {grade}. Anda mendapat A")
elif grade >= 80:
    print(f"grade anda {grade}. Anda mendapat B")
elif grade >= 70:
    print(f"grade anda {grade}. Anda mendapat C")
else:
    print(f"grade anda {grade}. Anda mendapat D")
