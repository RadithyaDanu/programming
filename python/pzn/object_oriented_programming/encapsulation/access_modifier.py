# pyhton pake naming conventions untuk nandain level akses
# 1. public attribute(default) bsia diakses dimana aja tanpa protection
# misal kita pengen ubah data saldo jadi -100 itu diperbolehkan
class BankAcc:
    norek = ""  # ini adalah contoh public attribute
    saldo = 0
    active = True

    def __init__(self, norek, saldo=0):
        self.norek = norek
        self.saldo = saldo

    @classmethod
    def disabled(cls, norek, saldo):
        result = cls(norek, saldo)
        result.active = False
        return result


bank = BankAcc("12345", 10000)
# ini bisa dijalanin karena akses attribute publik (bisa diubah siapapun)
bank.saldo = -1000
bank2 = BankAcc.disabled("33333", 20000)
print(
    f"bank acc {bank.norek} has balance {bank.saldo} and status {bank.active}")
print(
    f"bank acc {bank2.norek} has balance {bank2.saldo} and status {bank2.active}")

# 2.  protected attribute
# pake single underscore _, ini nandain convention atau tanda attribute ini untuk internal(jgn diakses)
# ex:


class Mahassiwa:
    _nama = ""

# nah nama itu merupakan protectedd attribute
# ini bisa diakses, tapi nandain ini untuk ngasih tau semua orang kalo ini internal
# jadi jangan diakses

# 3. private attribute
# pake double underscore __, python akan melakukan name mangling(pengubahan nama attribute dr luar)
# # sehingga attribute ini sulit diakses dari luar
# jadi kalo cuma pengen bikinattribut yang cmn bisa dipake dari class/object itu sendiri maka pakeini


class Nama:
    __name = ""

    def nama_saya(self):
        return self.__name


test = Nama()
print(test.__name)
