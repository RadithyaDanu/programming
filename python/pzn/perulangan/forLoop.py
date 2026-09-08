# digunakan untuk mengulang kode sesuai jumlah yang telah ditentukan atau mengiterasi melalui
# sekumpulan data. biasanya menggunakan range() untuk menentukan jumlah perulangan

for i in range(4):
    print(f"1perulangan ke-{i}")

for i in range(1, 5):
    print(f"2perulangan ke-{i}")

# range(start, stop, step) digunakan untuk menentukan jumlah perulangan
# 2 merupakan step antar index
for i in range(1, 10, 2):
    print(f"3perulangan ke-{i}")

for i in range(5, 0, -1):
    print(f"4perulangan ke-{i}")
