
testing = "ayam"
radit = "radit" if "ayam" in testing else "danu"
print(radit)

# lambda itu fungsi penampung sementara, dipake kalo kita langsung pengen operasiin
# tanpa hraus emmbuat variabel baru
# xontoh
# Pakai lambda


# kuadrat = lambda x: x ** 2
# print(kuadrat(5))  # Hasil: 25

angka = [1, 2, 3, 4]
# Mengalikan setiap angka dengan 2
hasil = list(map(lambda x: x * 2, angka))
# Hasil: [2, 4, 6, 8]
