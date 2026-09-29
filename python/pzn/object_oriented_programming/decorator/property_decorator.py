# property decorator
# bisa nandain setter dan getter dengan decorator @property
# habis itu kita bisa pake method tsb kyk pake attribute
# seakan akan kita pake attribute tapi pake method

# jadi kalo kita mau nambah validasi dengan konsep getter setter
# tapi kita aksesnya pengen kayak properti atau attribute biasa bisa pake @property

class Category:
    _name = ""  # pake _ dibawah supaya ngasih peringatan ga akses langsung

    # Getter
    @property
    def name(self):
        # @property membuat method ini bisa dipanggil
        # seperti attribute.
        return self._name

    # setter
    @name.setter  # name didapet dari method name diatas, kalo namenya diganti id jadi @id.setter
    def name(self, name):  # utk ngubah data namanya
        if name == "":  # kalo nama ygdiubbah disini adalah kosong maka namma gblh kosong
            raise ValueError("nama tidak boleh kosong")

        self._name = name

        # Setter digunakan ketika kita memberikan nilai
        # ke attribute name.


nama = Category()

# Setter otomatis dipanggil
nama.name = "Radit"

# Getter otomatis dipanggil
print(nama.name)

# Tanpa @property
# nama.set_name("Radit")
# print(nama.get_name())
