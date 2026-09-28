# keuntungan menggunakan constructor adalah, bisa nambahin validasi saat object pertama kali
# dibuat scr otomatis
# kita bisa cek nilai dari parameter, kalo ga valid, kita bisa raise error

class BankAcc:
    norek = ""
    saldo = 0

    def __init__(self, norek, saldo=0):

        if saldo < 0:
            raise ValueError("saldo tidak boleh kurang dari 0!")
            # validasi terlebih dahulu sebelum masuk

        self.norek = norek
        self.saldo = saldo


bank = BankAcc("12345", 1)
print(bank)
