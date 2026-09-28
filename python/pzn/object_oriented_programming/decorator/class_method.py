# erupakan method yang menerima class sebagai parameter pertama (biasanya dinamakan cls), bkn instance
# berguna biasanya untuk factory method, bikin object dirinya sendiri
# factory method atau class yang berhubungan denga class itu sendiri
# class method bisa akses class attribute tapi gabisa akses instance attribute

class BankAcc:
    norek = ""
    saldo = 0
    active = True

    def __init__(self, norek, saldo=0):
        self.norek = norek
        self.saldo = saldo

    @classmethod
    def disabled(cls, norek, saldo):  # disini parameternya bukan self tp cls
        result = cls(norek, saldo)  # jadi seakan akan cls ini adalah BankAcc
        # Ini akan membuat object baru dan otomatis
        # menjalankan constructor __init__().
        result.active = False
        return result
# seakan ketika  di kode ini result = cls(norek, saldo)
# ini kayak bikin object BankAcc baru dimmana dia manggil constructor __init__()
# parameternya itu ngakses dari __init__
# class method bisa mengakses instance attribute secara tidak
# langsung kalau dia membuat atau menerima sebuah object:


bank = BankAcc("12345", 10000)
bank2 = BankAcc.disabled("33333", 20000)
print(
    f"bank acc {bank.norek} has balance {bank.saldo} and status {bank.active}")
print(
    f"bank acc {bank2.norek} has balance {bank2.saldo} and status {bank2.active}")

# Class method bisa mengakses class attribute melalui cls, tetapi tidak bisa langsung mengakses
# instance attribute melalui self karena class method tidak menerima self.
