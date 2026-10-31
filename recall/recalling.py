from collections import defaultdict
from typing import List, Dict, Any

# Database sementara (In-Memory)
transactions: List[Dict[str, Any]] = [
    {"id": 1, "title": "Gaji Bulanan", "amount": 5000000.0,
        "type": "income", "category": "Salary", "tags": ["work"]},
    {"id": 2, "title": "Beli Kopi", "amount": 25000.0, "type": "expense",
        "category": "Food", "tags": ["coffee", "daily"]},
    {"id": 3, "title": "Bensin PCX", "amount": 50000.0,
        "type": "expense", "category": "Transport", "tags": ["vehicle"]},
    {"id": 4, "title": "Makan Siang", "amount": 35000.0,
        "type": "expense", "category": "Food", "tags": ["daily"]},
]


def add_transaction(title: str, amount: float, trans_type: str, category: str, tags: List[str]) -> None:
    # 1. Hitung ID baru secara aman (handling list kosong)
    new_id = transactions[-1]["id"] + 1 if transactions else 1

    # 2. Buat dictionary data & append ke list
    new_data: Dict[str, Any] = {
        "id": new_id,
        "title": title,
        "amount": amount,
        "type": trans_type.lower(),
        "category": category,
        "tags": [t.strip().lower() for t in tags]  # Clean whitespace tiap tag
    }
    transactions.append(new_data)
    print(
        f"\n[SUCCESS] Transaksi '{title}' berhasil ditambahkan dengan ID {new_id}!")


def filter_by_category(category: str) -> List[Dict[str, Any]]:
    # Query List Comprehension + Case Insensitive Filter
    return [t for t in transactions if t["category"].lower() == category.lower()]


def search_by_tag(tag: str) -> List[Dict[str, Any]]:
    # Query Cek ketersediaan elemen dalam list 'tags'
    return [t for t in transactions if tag.lower() in [t_tag.lower() for t_tag in t["tags"]]]


def calculate_summary() -> Dict[str, float]:
    # Query Agregasi pakai sum() dan List Comprehension
    total_income = sum(t["amount"]
                       for t in transactions if t["type"] == "income")
    total_expense = sum(t["amount"]
                        for t in transactions if t["type"] == "expense")
    return {
        "income": total_income,
        "expense": total_expense,
        "balance": total_income - total_expense
    }


def get_expenses_by_category() -> Dict[str, float]:
    # Query Pengelompokan data dengan defaultdict
    category_totals: Dict[str, float] = defaultdict(float)
    for t in transactions:
        if t["type"] == "expense":
            category_totals[t["category"]] += t["amount"]
    return dict(category_totals)


def get_top_expenses(n: int = 3) -> List[Dict[str, Any]]:
    # Query Filter + Sorting dengan Lambda (Descending)
    expenses = [t for t in transactions if t["type"] == "expense"]
    return sorted(expenses, key=lambda x: x["amount"], reverse=True)[:n]


# --- MENU INTERAKTIF CLI ---
if __name__ == "__main__":
    while True:
        print("\n" + "=" * 35)
        print("     PERSONAL EXPENSE TRACKER     ")
        print("=" * 35)
        print("1. Tambah Transaksi")
        print("2. Lihat Semua Transaksi")
        print("3. Cari Berdasarkan Kategori / Tag")
        print("4. Lihat Summary (Pemasukan, Pengeluaran, Saldo)")
        print("5. Keluar")

        try:
            user_input = int(input("Masukkan pilihan (1-5): "))
        except ValueError:
            print("[ERROR] Masukkan angka pilihan yang valid!")
            continue

        if user_input == 5:
            print("Sampai jumpa!")
            break

        if user_input == 1:
            print("\n--- Tambah Transaksi ---")
            try:
                title = input("Judul Transaksi : ").strip()
                amount = float(input("Jumlah (Rp)     : "))
                trans_type = input("Tipe (income/expense): ").strip()
                category = input("Kategori        : ").strip()
                raw_tags = input("Tags (pisahkan koma, misal: coffee,daily): ")

                tags_list = [t.strip()
                             for t in raw_tags.split(",") if t.strip()]

                add_transaction(title, amount, trans_type, category, tags_list)
            except ValueError:
                print("[ERROR] Jumlah uang harus berupa angka yang valid!")

        elif user_input == 2:
            print("\n--- Daftar Semua Transaksi ---")
            for t in transactions:
                print(
                    f"[{t['id']}] {t['title']} | Rp {t['amount']:,.0f} | {t['type'].upper()} | Cat: {t['category']} | Tags: {t['tags']}")

        elif user_input == 3:
            print("\n1. Filter Kategori | 2. Cari Tag")
            sub_choice = input("Pilih mode (1/2): ")
            if sub_choice == "1":
                cat = input("Masukkan nama kategori: ")
                results = filter_by_category(cat)
            else:
                tag = input("Masukkan tag: ")
                results = search_by_tag(tag)

            print(f"\nHasil Ditemukan ({len(results)} item):")
            for r in results:
                print(
                    f"- {r['title']} (Rp {r['amount']:,.0f}) [{r['category']}]")

        elif user_input == 4:
            summary = calculate_summary()
            print("\n--- FINANCIAL SUMMARY ---")
            print(f"Total Pemasukan   : Rp {summary['income']:,.0f}")
            print(f"Total Pengeluaran : Rp {summary['expense']:,.0f}")
            print(f"Sisa Saldo        : Rp {summary['balance']:,.0f}")

            print("\nPengeluaran per Kategori:")
            for cat, total in get_expenses_by_category().items():
                print(f"  - {cat}: Rp {total:,.0f}")
