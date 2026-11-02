transactions = [
    {"id": 1, "title": "Gaji", "amount": 5000000.0,
        "type": "income", "category": "Salary"},
    {"id": 2, "title": "Kopi", "amount": 25000.0,
        "type": "expense", "category": "Food"},
]

# // Buat fungsi add_transaction(title, amount, trans_type, category):

# // Logika ID: Cari ID transaksi terakhir.

# // Hint: Coba pakai for loop biasa untuk nyari id paling besar, ATAU periksa apakah list
# // transactions ada isinya (if len(transactions) > 0:). Kalau ada isi, ambil ID data terakhir lalu tambah 1.
# // Kalau kosong, set ID = 1.

# // Buat dictionary new_data yang menampung id, title, amount, trans_type, dan category.

# // Masukkan new_data ke dalam list transactions menggunakan .append().

# // Tes panggil fungsinya di bagian bawah script dengan data baru, lalu print(transactions)
# // buat mastiin datanya nambah dengan ID = 3.


def add_transaction(title: str, amount: float, trans_type: str, category: str):
    last_id = transactions[-1]["id"] + 1 if transactions else 1

    new_data = {"id": last_id, "title": title, "amount": amount,
                "type": trans_type, "category": category}
    transactions.append(new_data)


data = add_transaction("a", 1000, "income", "aya")
print(transactions)


# 📜 Tugas Tahap 2: Menampilkan & Memfilter Data
# Tambahkan 2 fungsi ini di bawah kode Tahap 1 lu kemarin:
# 1. show_all_transactions() (Fungsi Void)
# Loop setiap elemen di list transactions.
# Cetak data tersebut menggunakan print() dan F-Strig yang rapi.
# Contoh Output: [ID: 1] Gaji - Rp 5000000.0 (income)
# 2. filter_by_type(target_type: str) (Fungsi Return)
# Buat list penampung kosong results = [].
# Loop transactions, jika type pada transaksi sama dengan target_type (misal "expense"),
# masukkan data transaksi tersebut ke results memakai .append().
# Tips: Gunakan .lower() saat membandingkan string biar case-insensitive
# (misal: "Expense" atau "expense" tetap terbaca sama).
# Kembalikan (return) list results.

# # Uji Coba Tahap 2
# show_all_transactions()

# pengeluaran = filter_by_type("expense")
# # Karena ini fungsi Return, hasilnya ditampung dulu di variabel 'pengeluaran'
# print("Hasil Filter Expense:", pengeluaran)


def show_all_transactions():
    for i, items in enumerate(transactions):
        print(
            f"{items['id']}. {items['title']} - {items['amount']} ({items['type']}) ")


# def filter_by_type():
#     expense = sum(t['amount'] for t in transactions if t['type'] == "expense")
#     income = sum(t['amount'] for t in transactions if t['type'] == "income")
#     balance = income - expense
#     print(
#         f"pengeluaran = {expense}\n pemasukan = {income}\n sisa saldo = {balance}")

# val1 = items['amount'] if items['type'] == 'expense' else none
#             data.append(val1)

def filter_by_type(target_type: str):
    data = []
    for i, items in enumerate(transactions):
        if items['type'].lower() == target_type.lower():
            data.append(items)

    return data


pengeluaran = filter_by_type("expense")
print("Hasil Filter Expense:", pengeluaran)


# 📜 Tugas Lu di Tahap 3:
# Buat fungsi calculate_summary() (Fungsi Return):
# Buat 2 variabel akumulator awal: total_income = 0.0 dan total_expense = 0.0.
# Loop list transactions:
# Jika items["type"] == "income", tambahkan items["amount"] ke total_income.
# Jika items["type"] == "expense", tambahkan items["amount"] ke total_expense.
# Hitung balance = total_income - total_expense.
# Kembalikan (return) dalam bentuk dictionary:
# Python
# return {
#     "total_income": total_income,
#     "total_expense": total_expense,
#     "balance": balance
# }

def calculate_summary():
    total_expense = sum(t['amount']
                        for t in transactions if t['type'] == "expense")
    total_income = sum(t['amount']
                       for t in transactions if t['type'] == "income")
    balance = total_income - total_expense
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }


itung = calculate_summary()
print(itung['balance'])
