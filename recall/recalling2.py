transactions = [
    {"id": 1, "title": "Gaji", "amount": 5000000.0,
        "type": "income", "category": "Salary"},
    {"id": 2, "title": "Kopi", "amount": 25000.0,
        "type": "expense", "category": "Food"},
    {"id": 3, "title": "Kopi", "amount": 25000.0,
     "type": "expense", "category": "Food"},
    {"id": 4, "title": "Kopi", "amount": 25000.0,
     "type": "expense", "category": "Food"}
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
print("===========================================")

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


print("===========================================")
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
print("===========================================")

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
print(itung)
print("===========================================")

# Tujuannya: Menghitung total pengeluaran untuk tiap-tiap kategori secara dinamis
# (misal: Food, Transport, Salary, dll).
# 📜 Tugas Lu di Tahap 4:
# Buat fungsi get_expenses_by_category() (Fungsi Return):
# Buat dictionary kosong buat nampung hasil pengelompokan: category_totals = {}.
# Loop setiap items di dalam transactions:
# Cek dulu: hanya proses jika items["type"] == "expense".
# Ambil nama kategorinya (cat = items["category"]) dan jumlahnya (amt = items["amount"]).
# Logika Pengelompokan:
# Jika cat sudah ada di dalam dictionary category_totals: tambahkan amt ke nilai yang sudah ada (category_totals[cat] += amt).
# Jika cat belum ada: buat key baru dan isi nilainya dengan amt (category_totals[cat] = amt).
# Kembalikan (return) dictionary category_totals.
# Expected Output:
# Jika ada transaksi Food sebesar 25.000 dan Food sebesar 35.000, hasilnya harus berisi {"Food": 60000.0}.


def get_expenses_by_category():
    category_totals = {}

    for items in transactions:
        # 1. Filter hanya yang bertipe 'expense'
        if items['type'] == "expense":
            cat = items['category']
            amt = items['amount']

            # 2. Cek apakah nama kategori (misal "Food") sudah ada di dict?
            if cat in category_totals:
                # Jika sudah ada, TAMBAHKAN nilainya
                category_totals[cat] += amt
            else:
                # Jika belum ada, BUAT KEY BARU dengan nilai awal amt
                category_totals[cat] = amt

    return category_totals


testing = get_expenses_by_category()
print(testing)


# Bikin blok menu utama di bagian paling bawah script (if __name__ == "__main__":):
# Gunakan while True: biar menunya muncul terus sampai user memilih menu Keluar.
# Tampilkan pilihan menu:
# 1. Tambah Transaksi
# 2. Lihat Semua Transaksi
# 3. Filter Transaksi (income/expense)
# 4. Lihat Ringkasan (Summary & Pengeluaran per Kategori)
# 5. Keluar
# Gunakan try-except ValueError saat meminta input pilihan angka dari user biar kalau user ngetik huruf (misal "abc"),
# program gak crash tapi nampilin pesan error: "Input harus berupa angka!".
# Hubungkan pilihan menu tersebut ke fungsi-fungsi yang udah kita buat dari Tahap 1 sampai 4!

if __name__ == "__main__":
    while True:
        print("1. Tambah Transaksi")
        print("2. Lihat Semua Transaksi")
        print("3. Filter Transaksi (income/expense)")
        print("4.  Lihat Ringkasan (Summary & Pengeluaran per Kategori)")
        print("5. Keluar")
        print("============================================")

        try:
            user_input: int = int(input("masukkan pilihan : "))
        except ValueError:
            print("masukkan input yang valid!")
            continue

        if user_input not in [1, 2, 3, 4, 5]:
            print("pilih angka yang benar")
            continue

        if user_input == 1:
            try:
                input1: str = input("title = ")
                input2: float = int(input("amount = "))
                input3: str = input("type = ")
                input4: str = input("category = ")
            except ValueError:
                print("masukkan input yang valid!")

            storage = add_transaction(input1, input2, input3, input4)
            print(storage)
            print("==================================")

        if user_input == 2:
            show_all_transactions()
            print("==================================")

        if user_input == 3:
            input_user: str = input("tipe transaksi = ").lower()
            if input_user not in ['income', 'expense']:
                print('tipe tidak tersedia, periksa lagi!')
                continue

            pengeluaran = filter_by_type(input_user)
            print(pengeluaran)
            print("==================================")

        if user_input == 4:
            storage = get_expenses_by_category()
            print(storage)
            print("==================================")

transactions = [
    {"id": 1, "title": "Gaji", "amount": 5000000.0,
        "type": "income", "category": "Salary"},
    {"id": 2, "title": "Kopi", "amount": 25000.0,
        "type": "expense", "category": "Food"},
    {"id": 3, "title": "Bensin PCX", "amount": 50000.0,
        "type": "expense", "category": "Transport"},
]


def add_transaction(title: str, amount: float, trans_type: str, category: str):
    last_id = transactions[-1]["id"] + 1 if transactions else 1
    new_data = {
        "id": last_id,
        "title": title,
        "amount": amount,
        "type": trans_type.lower(),
        "category": category
    }
    transactions.append(new_data)
    print(f"\n[INFO] Transaksi '{title}' berhasil ditambahkan!")


def show_all_transactions():
    print("\n--- DAFTAR SEMUA TRANSAKSI ---")
    for items in transactions:
        print(f"[{items['id']}] {items['title']} - Rp {items['amount']:,.0f} ({items['type']}) | Cat: {items['category']}")


def filter_by_type(target_type: str):
    data = []
    for items in transactions:
        if items['type'].lower() == target_type.lower():
            data.append(items)
    return data


def calculate_summary():
    total_expense = sum(t['amount']
                        for t in transactions if t['type'].lower() == "expense")
    total_income = sum(t['amount']
                       for t in transactions if t['type'].lower() == "income")
    balance = total_income - total_expense
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }


def get_expenses_by_category():
    category_totals = {}
    for items in transactions:
        if items['type'].lower() == "expense":
            cat = items['category']
            amt = items['amount']
            if cat in category_totals:
                category_totals[cat] += amt
            else:
                category_totals[cat] = amt
    return category_totals


if __name__ == "__main__":
    while True:
        print("\n============================================")
        print("1. Tambah Transaksi")
        print("2. Lihat Semua Transaksi")
        print("3. Filter Transaksi (income/expense)")
        print("4. Lihat Ringkasan (Summary & Pengeluaran per Kategori)")
        print("5. Keluar")
        print("============================================")

        try:
            user_input = int(input("Masukkan pilihan (1-5): "))
        except ValueError:
            print("[ERROR] Masukkan input angka yang valid!")
            continue

        if user_input == 5:
            print("Terima kasih! Program selesai.")
            break

        if user_input not in [1, 2, 3, 4, 5]:
            print("[ERROR] Pilih angka antara 1-5!")
            continue

        if user_input == 1:
            try:
                title = input("Title    : ").strip()
                amount = float(input("Amount   : "))
                trans_type = input("Type (income/expense): ").strip()
                category = input("Category : ").strip()
                add_transaction(title, amount, trans_type, category)
            except ValueError:
                print("[ERROR] Amount harus berupa angka!")

        elif user_input == 2:
            show_all_transactions()

        elif user_input == 3:
            input_user = input(
                "Tipe transaksi (income/expense): ").strip().lower()
            if input_user not in ['income', 'expense']:
                print('[ERROR] Tipe tidak valid! Pilih income atau expense.')
                continue

            hasil_filter = filter_by_type(input_user)
            print(f"\n--- Hasil Filter ({input_user}) ---")
            for t in hasil_filter:
                print(
                    f"- {t['title']}: Rp {t['amount']:,.0f} [{t['category']}]")

        elif user_input == 4:
            summary = calculate_summary()
            category_totals = get_expenses_by_category()

            print("\n--- RINGKASAN KEUANGAN ---")
            print(f"Total Pemasukan   : Rp {summary['total_income']:,.0f}")
            print(f"Total Pengeluaran : Rp {summary['total_expense']:,.0f}")
            print(f"Sisa Saldo        : Rp {summary['balance']:,.0f}")

            print("\n--- Pengeluaran per Kategori ---")
            for cat, total in category_totals.items():
                print(f"- {cat}: Rp {total:,.0f}")
