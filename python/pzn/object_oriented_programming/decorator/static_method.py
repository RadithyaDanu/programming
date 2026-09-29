# independent function
# method yg berdiri sendiri(independen)
# utk akses static method, gaperlu pake object, bisa langsung pake classnya tanpa harus bikin objectnya
# statis method gabisa akses class attribute atau instance/object attribute

# murni function independen, kayak function biasa tapi nempel di class
# tinggal nambahin @staticmethod pada method yg dibikin iut

class Matematika:

    @staticmethod
    def tambah(a, b):
        return a+b


# dengan gini, kita gaperlu bikin object dulu, jadi bisa langsung manggil classnya aja
print(Matematika.tambah(10, 2))
