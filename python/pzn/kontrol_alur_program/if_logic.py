# kondisi harus bernilai boolean, jadi kita bisa pake operator perbandingan dan operator logika
# and, or, not.

# and
umur = int(input("masukin umur = "))
sim = input("apakah punya sim? (y/n) = ")
if umur >= 18 and sim == "y":
    print("boleh nyetir")
else:
    print("tidak boleh nyetir")

# or
nilai = int(input("masukin nilai "))
if nilai >= 80 or nilai == 75:
    print("lulus")
else:
    print("tidak lulus")
