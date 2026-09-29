class Category:
    _name = ""  # pake _ dibawah supaya ngasih peringatan ga akses langsung

    # setter
    def set_name(self, name):  # utk ngubah data namanya
        if name == "":  # kalo nama ygdiubbah disini adalah kosong maka namma gblh kosong
            raise ValueError("nama tidak boleh kosong")
        self._name = name

    # getter
    def get_name(self):  # kalo mau akses _name, gunakan ini
        return self._name


nama = Category()
nama.set_name('radit')
print(nama.get_name())
# sebnernya ini kayak object biasa aja sih, tapi biar lebih enak aja
