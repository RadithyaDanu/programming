# menempatkan perulangan di dalam perulangan
# for dalam for, while dalam while, while dalam for, for dalam while

print("tabel perkalian 1-5")
for i in range(1, 6):
    for j in range(1, 6):
        hasil = i * j
        print(f"{i} x {j} = {hasil}")
