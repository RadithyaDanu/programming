# mencari password dengan batasan percobaan

password = "radit"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    pasws = input("masukkan password : ")
    percobaan += 1
    if pasws == password:
        print("selamat datang")
        break
    else:
        print(f"password salah, sisa percobaan {max_percobaan - percobaan}")
else:
    print("terlalu banyak percobaan, coba lagi nanti")
