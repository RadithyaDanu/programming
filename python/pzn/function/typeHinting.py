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

# jadi hanya ngasih info mengenai tipe data yang diharapkan dari suatu value yang dibutuhkan dari suatu variabel tsb

# contoh penggunaan pada list

angka: list[int] = [1, 2, 3, 4, 5]
# jadi tipe data yang diinginkan adalah list, di dalam list tentu memiliki tipe data lagi
# int menjadi tipe data yang diinginkan di dalam list tersebut, jadi di dalam list hanya diperbolehkan menggunakan intn

nama: dict[str, int] = {"nama": "radithya",
                        "umur": 20}

# tapi, py tetap dynamic typing, penggunaan type hinting hanya jadi informasi tipe data yang diharapkan pada suatu
# variabel dan function
