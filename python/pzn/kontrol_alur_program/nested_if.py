# memasukkan if di dalam if lain
# misal kita pengen veerifikasi masuk akun
username = str(input("masukkan username = "))
password = input("masukkan password")

if username == "radit":
    if password == "1234":
        print("login berhasil")
    else:
        print("password salah")
else:
    print("username  salah")
