test = [{"nama": "radit",
         "umur": 21,
         "kelas": "3 sd"},
        {"nama": "danu",
         "umur": 30,
         "kelas": 99}]


print(test)

for i in test:
    for key, value in i.items():
        print(key, ":", value)
