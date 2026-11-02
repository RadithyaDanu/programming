# ==============================================================================
#                 PYTHON TRICKS & HIDDEN GEMS CHEATSHEET
#              (Fitur & Sintaksis yang Sering Dilupakan Orang)
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. ADVANCED LIST COMPREHENSIVE & GENERATORS
# ------------------------------------------------------------------------------
# If-Else di dalam List Comprehension (Posisi 'if-else' BEDA dengan 'if' filter biasa)
nums = [1, 2, 3, 4, 5, 6]
labels = ["Even" if x % 2 == 0 else "Odd" for x in nums]  # Filter + Transform

# Flattening Nested List (2D ke 1D)
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]  # [1, 2, 3, 4, 5, 6]

# Generator Expression (Ganti [] dengan () -> Hemat RAM buat data ribuan/jutaan)
huge_sum = sum(x * x for x in range(1000000))  # Tanpa alokasi list di memory


# ------------------------------------------------------------------------------
# 2. TYPE ANNOTATIONS & TYPE HINTING ADVANCED
# ------------------------------------------------------------------------------
from typing import Optional, Union, Callable

# Union / Optional (Bisa multi-tipe atau boleh None)
# Di Python 3.10+ bisa pakai operator pipe '|' yang lebih bersih:
def process_id(user_id: int | str) -> str:
    return f"ID_{user_id}"

# Default None value (Optional)
def get_user(user_id: int) -> str | None:
    return "Radit" if user_id == 1 else None

# Callable (Fungsi yang menerima fungsi lain sebagai argumen)
def execute_func(action: Callable[[int, int], int], a: int, b: int) -> int:
    return action(a, b)


# ------------------------------------------------------------------------------
# 3. UNPACKING & DESTRUCTURING (TRICK * & **)
# ------------------------------------------------------------------------------
# Extended Unpacking (Mengambil head, middle, tail)
first, *middle, last = [10, 20, 30, 40, 50]
# first = 10, middle = [20, 30, 40], last = 50

# Merging Dictionary instan pakai ** (Python 3.9+ bisa pakai operator '|')
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 99, "c": 3}  # 'b' bakal tertimpa nilai dict2
merged = dict1 | dict2    # {'a': 1, 'b': 99, 'c': 3}


# ------------------------------------------------------------------------------
# 4. DICTIONARY & SET HIDDEN FEATURES
# ------------------------------------------------------------------------------
from collections import defaultdict

# dict.setdefault() -> Set default value kalau key belum ada tanpa import modul
counts = {}
counts.setdefault("apples", []).append(1)  # Otomatis bikin list baru jika 'apples' ga ada

# Operator Set untuk Komparasi Data Cepat (Sangat Cepat O(1))
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

intersection = set_a & set_b  # {3, 4} (Elemen yang ada di keduanya)
difference = set_a - set_b    # {1, 2} (Elemen yang HANYA ada di set_a)
symmetric_diff = set_a ^ set_b# {1, 2, 5, 6} (Elemen yang tidak beririsan)


# ------------------------------------------------------------------------------
# 5. CONTEXT MANAGERS & ERROR HANDLING TRICKS
# ------------------------------------------------------------------------------
import contextlib

# Suppress Exception (Abaikan error tertentu tanpa ngetik try-except berantakan)
with contextlib.suppress(FileNotFoundError):
    import os
    os.remove("file_ga_ada.txt")  # Ga bakal bikin app crash kalau file ga ada

# Else pada Try-Except (Jalan HANYA JIKA TIDAK ADA ERROR di blok 'try')
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Sukses tanpa error, hasil: {result}")


# ------------------------------------------------------------------------------
# 6. FOR-ELSE LOOP (SERING BIKIN BINGUNG TAPI BIKIN KODE CLEAN)
# ------------------------------------------------------------------------------
# Blok 'else' pada 'for loop' jalan HANYA JIKA loop selesai TANPA kena 'break'
items = [1, 3, 5, 7]
target = 4

for item in items:
    if item == target:
        print("Ditemukan!")
        break
else:
    # Jalan kalau 'target' tidak ditemukan sama sekali di loop
    print("Item tidak ditemukan dalam list.")


# ------------------------------------------------------------------------------
# 7. BUILT-IN FUNCTIONS YANG JARANG DIMANFAATKAN
# ------------------------------------------------------------------------------
# zip() dengan Unpacking buat Transpose Matriks
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = list(zip(*matrix))  # [(1, 4), (2, 5), (3, 6)]

# any() & all() buat Cek Kondisi Multi-Elemen
numbers = [2, 4, 6, 8]
all_even = all(n % 2 == 0 for n in numbers)  # True (Apakah SEMUA genap?)
has_odd  = any(n % 2 != 0 for n in numbers)  # False (Apakah ADA SATU SAJA yang ganjil?)

# Walrus Operator := (Assign nilai variabel sekaligus pakai di dalam kondisi)
# Bikin kode lebih hemat baris saat baca stream / loop
data = ["apple", "banana", "cherry"]
if (length := len(data)) > 2:
    print(f"List memiliki {length} elemen")