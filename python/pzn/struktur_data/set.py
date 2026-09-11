# kumpulan data yang tidak berurutan
# list berurutan tapi set ngga
# bedanya dengan list ini tidak memiliki elemen yang duplikat
# kalo ada input data duplikat, maka hanya akan dicetak 1 data saja
# set ditulis dengan kurawal {} atau func set()
# sama kayak dict, tapi kalo dict kan declare keynya
# nambah data di set pake add(value), kalo nambah data kesini belum tentu datanya paling akhir krn konsepnya acak
# untuk hpaus data di  set, bisa pake remove(value). krn data ga berurut, jd gapunya index
# gabisa diakses dengan index, untuk akses datanya biasanya pake for

buah = {'mangga', 'apel', 'pisang'}
print(buah)
buah.add('semangka')
buah.add('semangka')
print(buah)

# hapus value di set
buah.remove('apel')
print(buah)

# nampiin elemen
for i in buah:
    print(i)
