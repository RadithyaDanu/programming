
sales = [
    {
        "transaction_id": "TR001",
        "product": "Kaos Kaki Sekolah",
        "price": 12000,
        "quantity": 10,
        "discount": 0.05
    },
    {
        "transaction_id": "TR002",
        "product": "Kaos Kaki Sport",
        "price": 18000,
        "quantity": 5,
        "discount": 0.00
    },
    {
        "transaction_id": "TR003",
        "product": "Kaos Kaki Polos",
        "price": 15000,
        "quantity": 8,
        "discount": 0.10
    },
    {
        "transaction_id": "TR004",
        "product": "Kaos Kaki Sekolah",
        "price": 12000,
        "quantity": 15,
        "discount": 0.05
    },
    {
        "transaction_id": "TR005",
        "product": "Kaos Kaki Sport",
        "price": 18000,
        "quantity": 7,
        "discount": 0.00
    },
    {
        "transaction_id": "TR006",
        "product": "Kaos Kaki Polos",
        "price": 15000,
        "quantity": 4,
        "discount": 0.00
    },
    {
        "transaction_id": "TR007",
        "product": "Kaos Kaki Sekolah",
        "price": 12000,
        "quantity": 20,
        "discount": 0.10
    },
    {
        "transaction_id": "TR008",
        "product": "Kaos Kaki Sport",
        "price": 18000,
        "quantity": 10,
        "discount": 0.05
    },
    {
        "transaction_id": "TR009",
        "product": "Kaos Kaki Polos",
        "price": 15000,
        "quantity": 12,
        "discount": 0.00
    },
    {
        "transaction_id": "TR010",
        "product": "Kaos Kaki Sekolah",
        "price": 12000,
        "quantity": 25,
        "discount": 0.05
    }
]


# for i in range(len(sales)):
#     print(sales[i]['price'], sales[i]['quantity'], sales[i]['discount'])

def calculate_revenue(price, quantity, discount):
    return price * quantity * (1 - discount)


for i, item in enumerate(sales):
    harga = item['price']
    quantity = item['quantity']
    diskon = item['discount']

    total_harga = calculate_revenue(harga, quantity, diskon)
    print(f"{item['transaction_id']} {item['product']} revenue : {total_harga}")

total = 0

for i, item in enumerate(sales):
    total += calculate_revenue(item['price'],
                               item['quantity'], item['discount'])

print(total)
