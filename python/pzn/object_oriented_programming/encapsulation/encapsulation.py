class BankAccount:
    __no = ""
    __balance = 0

    def __init__(self, no):
        self.__no = no

    @property
    def get_balance(self):
        return self.__balance

    # misal kita pengen bikin getter untuk ngambil data no juga
    @property
    def get_no(self):
        return self.__no

    def topup(self, amount):
        self.__balance += amount

    def cashout(self, amount):
        if amount > self.__balance:
            raise ValueError("gabisa narik, saldo lau kureng")

        self.__balance -= amount

# kenapa balance gamasuk ke constructor(__init), karena supaya pas pertama bikin akun
# saldo/balance defaultnya langsung 0
# kalo masuk constructor, otomamtis harus declare saldonya langsung
# jadi disini kita gapake setter karena kalo mau ngubah saldo harus topup


radit_account = BankAccount("radit")
radit_account.topup(100000)
print(radit_account.get_no)
print(radit_account.get_balance)
# jadi setelah property @property, gaperlu pake () lagi dalam pemanggilan methodnya
