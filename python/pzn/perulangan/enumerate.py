# jika kita ingin mendapatkan index dan data pada list dengan looping
# biasanya kita akan melakukan seperti ini
#
# dummmy = ["radithya", "danu", "tirta"]
# for i in range(len(dummy)):
#     print(f"{i}. : {dummy[i]}")
#
# cara dibawah ini lebih gampang pake enumerate

dummmy = ["radithya", "danu", "tirta"]

for i, item in enumerate(dummmy):
    print(f"{i} : {item}")

# dibawah ini kalo list berisi dict
# kasusnya pengen ngasih index ke dict di output
test = [{"nama": "radit",
         "umur": 21,
         "kelas": "3 sd"},
        {"nama": "danu",
         "umur": 30,
         "kelas": 99}]

for i, items in enumerate(test):
    print(f"{i + 1}. {items["nama"]}")
