test = [{"nama": "radit",
         "umur": 21,
         "kelas": "3 sd"},
        {"nama": "danu",
         "umur": 30,
         "kelas": 99}]


for i in range(len(test)):
    hasil = f"{i + 1}. {test[i]["nama"]}"


splitting = hasil.split('.')
data_hasil = int(splitting[0])
print(data_hasil)
# user_input = input("masukkan data yang ingin dihapus : ")

# if user_input == data_hasil:
#     hapus = data[data_hasil]
#     del data[data_hasil]
#     print(f"data {hapus} telah dihapus!")


# # print(test[0]["nama"])
# print(test["nama"][0])

# # objek = test[0]["umur"]
# # objek2 = test[1]["umur"]
# # print(objek + objek2)
# # # print(test)

# # for i in test:
# #     for key, value in i.items():
# #         print(key, ":", value)
