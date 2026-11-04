import pandas as pd
import numpy as np

# 1. SETUP DATASET MENTAH (Simulasi Data Transaksi)
raw_data = {
    "transaction_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "date": ["2026-10-01", "2026-10-02", "2026-10-02", "2026-10-03", "2026-10-05", "2026-10-05", "2026-10-06", "2026-10-07"],
    "title": ["Gaji Bulanan", "Beli Kopi", "Bensin PCX", "Makan Siang", "Token Listrik", "Kopi & Snack", "Freelance Project", "Servis Motor"],
    # Ada data hilang (NaN)
    "amount": [5000000, 25000, 50000, 35000, 100000, 45000, 1500000, np.nan],
    "type": ["income", "expense", "expense", "expense", "expense", "expense", "income", "expense"],
    "category": ["Salary", "Food", "Transport", "Food", "Bills", "Food", "Side Income", "Transport"]
}

# Load ke Pandas DataFrame
df = pd.DataFrame(raw_data)
print(df.head())

# # ------------------------------------------------------------------------------
# # TAHAP 1: DATA CLEANING (Pembersihan Data)
# # ------------------------------------------------------------------------------
# # TODO 1.1: Cek berapa banyak data NaN (missing values) di setiap kolom
# # Hint: gunakan df.isnull().sum()
# print(df.isnull().sum())

# # TODO 1.2: Isi data NaN pada kolom 'amount' dengan angka 0 atau median pengeluaran
# # Hint: df['amount'] = df['amount'].fillna(0)
# df['amount'] = df['amount'].fillna(0)

# df = df.fillna({'amount': 0})
# print(df)

# df['amount'] = df['amount'].fillna(df['amount'].median())
# # ------------------------------------------------------------------------------
# # TAHAP 2: FILTERING & QUERYING (Penyaringan Data)
# # ------------------------------------------------------------------------------
# # TODO 2.1: Filter hanya transaksi yang bertipe 'expense'
# # expenses_df = ...

expense_df = df[df['type'] == 'expense']
# seluruh dataframe masuk ke expense df tapi filter tipe expense

# big_expense = df[(df['type'] == 'expense') and (df['amount'] > 40000)]
# pake & bukan and, intinya di pandas pakenya simbol
# TODO 2.2: Filter pengeluaran yang nominalnya di atas Rp 40,000
# big_expenses = ...

big_expenses = expense_df[expense_df["amount"] > 40000]
print(big_expenses)


# ------------------------------------------------------------------------------
# TAHAP 3: AGREGASI & GROUPBY (Pengelompokan Data)
# ------------------------------------------------------------------------------
# TODO 3.1: Hitung total amount berdasarkan 'type' (income vs expense)
#
summary = df.groupby('type')['amount'].sum()
print(summary)

# TODO 3.2: Hitung total pengeluaran per 'category' lalu urutkan dari yang terbesar
# category_summary = ...

cat_sum = df.groupby('category')['amount'].sum()
# print(cat_sum.sort_values(by='amount', ascending=False))
# kalo groupby ini bener, karena ad apencarian amount disitu
# kalo series ini salah, karena series hanya 1 kolom data aja
# yg bener :
print(cat_sum.sort_values(ascending=False))

# ------------------------------------------------------------------------------
# TAHAP 4: FEATURE ENGINEERING / KOLOM BARU
# ------------------------------------------------------------------------------
# TODO 4.1: Tambahkan kolom baru 'amount_usd' (asumsi 1 USD = Rp 15,000)
# df['amount_usd'] = df['amount'] / 15000
df['amount_usd'] = df['amount']/15000

# TODO 4.2: Tambahkan kolom status 'high_transaction' (True jika amount > 1,000,000)
#
df['high_transaction'] = df['amount'] > 1000000


# # --- TEST OUTPUT HASIL ---
if __name__ == "__main__":
    print("=== HASIL AKHIR DATAFRAME ===")
    print(df)
