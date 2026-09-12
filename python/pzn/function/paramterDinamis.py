# paramter jd dinamis, ga harus ditentukan jumlahnya
# tambahin tanda * sebelum nama parameter untuk nandain ini adalah paramter dinamis berupa list
# atau pake tanda ** untuk nandain ini adalah paramter dinamis berupa dictionary

# list function
def cetak_list(*list):  # tambahin tanda * sebelum nama paramter
    for item in list:  # harus pake for karena ini tipenya list, kalo gapake outputnya bakal ada kurung
        print(item)
# jadi bisa panggil argumen banyak


cetak_list(1, 2, 3, 4, 5, 6)  # datanya akan dijadiin satu

# dictionary


def cetak_dict(**dict):
    for key, value in dict.items():
        print(key, ":", value)


cetak_dict(nama="radit", umur=20)
