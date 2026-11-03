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
