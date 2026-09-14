# kita pengen input dari user itu tipe datanya ditentukan dan outputnya juga ditentukan
# misal kita pengen input dan output dari program kita adalah integer, maka perlu dituliskan seperti ini

def tambah(a: int, b: int) -> int:
    return a + b


pertambahan = tambah(9, 9)
print(pertambahan)


# ga cuma parameter function, variabel juga bisa pake type hinting ini
# misal
nama: str = "radit"
umur: int = 20
tinggi: float = 175.6
isMarried: bool = False
