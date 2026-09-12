# kita pengen ngebuat si function tsb ngelakuin suatu kegiatan dan  hasil kegiatan tersebut ingin kita dapatkan
# function bisa mengembalikan nilai dari kegiatan yang sudah dilakukan pada function tsb
# pake kata kunci return
# setelah kata kunci return, diikut dengan nilai yang ingin dikembalikan di function tsb

def lingkaran(radius):
    pi = 3.14
    luas = pi * radius * radius
    return luas


# pas kita manggil function dengan return value, kita bisa simpen hasil return valuenya di dalam variabel
luas1 = lingkaran(10)
luas2 = lingkaran(3)
print(f"luas lingkaran 1 = {luas1}\nluas lingkaran 2 = {luas2}")
