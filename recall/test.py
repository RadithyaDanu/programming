# # nums = [1, 5, 7, 8, 10]


# # # ada 2 konsep loop untuk ambil key value
# # # for i, num in enumerate(nums):
# # #     print(i, num)

# # # for i in range(len(nums)):
# # #     print(i, nums[i])
# # huge_sum = sum(x * x for x in range(10))

# # print(huge_sum)


# inpu = input("masukin : ", "masukin 2 : ", "masukin 3 : ")
# print(inpu)

transactions = [
    {"id": 1, "title": "Gaji", "amount": 5000000.0,
        "type": "income", "category": "Salary"},
    {"id": 2, "title": "Kopi", "amount": 25000.0,
        "type": "expense", "category": "Food"},
    {"id": 3, "title": "Bensin PCX", "amount": 50000.0,
        "type": "expense", "category": "Transport"},
]

for i in transactions:
    print(i['id'])
