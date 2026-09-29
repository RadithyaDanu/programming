# Soal Recall Python (Non-OOP)

Materi yang dicakup: operator, kontrol alur, perulangan, function,
struktur data, string manipulation, error handling, file I/O.

Cara pengerjaan:
- Soal "teori" → jawab pakai kalimatmu sendiri
- Soal "prediksi output" → tulis dulu jawabanmu SEBELUM menjalankan kodenya
- Soal "coding" → tulis kodenya di file .py terpisah

---

## Bagian 1 — Operator

**1.1 (teori)** Apa perbedaan operator `/`, `//`, dan `%`? Berikan contoh angka 10 dan 3.

**1.2 (prediksi output)** Tulis hasil dari setiap baris:
```python
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(2 ** 3)
```

**1.3 (prediksi output)**
```python
x = 5
x += 3
x *= 2
print(x)
```

**1.4 (prediksi output)**
```python
print(5 > 3)
print(5 == "5")
print(True and False)
print(not (10 > 2))
print(3 > 2 > 1)
```

**1.5 (teori)** Apa yang terjadi jika menjumlahkan string `"10" + 5`? Bagaimana cara memperbaikinya?

---

## Bagian 2 — Kontrol Alur (if / match-case)

**2.1 (prediksi output)**
```python
nilai = 75

if nilai >= 90:
    print("A")
elif nilai >= 70:
    print("B")
elif nilai >= 50:
    print("C")
else:
    print("D")
```

**2.2 (prediksi output)**
```python
umur = 20
punya_ktp = False

if umur >= 17:
    if punya_ktp:
        print("boleh ikut pemilu")
    else:
        print("buat ktp dulu")
else:
    print("belum cukup umur")
```

**2.3 (prediksi output)**
```python
hari = "senin"

match hari:
    case "senin" | "selasa":
        print("awal pekan")
    case "sabtu" | "minggu":
        print("weekend")
    case _:
        print("hari biasa")
```

**2.4 (coding)** Buat program yang menerima input angka bulan (1-12) lalu
cetak jumlah hari dalam bulan tersebut. Anggap Februari = 28 hari.
Gunakan `match-case`.

**2.5 (coding)** Buat program cek tahun kabisat:
- Habis dibagi 4 DAN tidak habis dibagi 100 → kabisat
- Habis dibagi 400 → kabisat

---

## Bagian 3 — Perulangan

**3.1 (prediksi output)**
```python
for i in range(1, 6):
    print(i * i)
```

**3.2 (prediksi output)** Berapa kali "halo" tercetak, dan mengapa?
```python
i = 0
while i < 10:
    print("halo")
    i += 3
```

**3.3 (prediksi output)**
```python
for i in range(5):
    if i == 3:
        continue
    if i == 4:
        break
    print(i)
print("selesai")
```

**3.4 (prediksi output)** Apa output program ini?
```python
angka = [7, 8, 9]

for a in angka:
    pass
else:
    print("loop selesai tanpa break")
```

**3.5 (prediksi output)**
```python
buah = ["apel", "jeruk", "mangga"]

for index, nama in enumerate(buah, start=1):
    print(f"{index}. {nama}")
```

**3.6 (prediksi output)** Apa output segitiga ini?
```python
for i in range(1, 4):
    print("*" * i)
```

**3.7 (coding)** Cetak tabel perkalian 1-10 untuk angka 7, format: `7 x 1 = 7`.

**3.8 (coding)** Hitung faktorial dari angka input user menggunakan `while` loop.
Contoh: 5! = 120.

**3.9 (coding)** Buat pola berikut menggunakan nested loop:
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

**3.10 (coding — challenge)** Buat program yang menerima satu angka `n`,
lalu cetak semua bilangan prima dari 2 sampai `n`. Gunakan `for-else`
untuk cek prima-nya.

---

## Bagian 4 — Function

**4.1 (teori)** Apa perbedaan `print()` dan `return` di dalam function?

**4.2 (prediksi output)**
```python
def sapa(nama="tamu"):
    print(f"halo {nama}")

sapa()
sapa("radit")
sapa(nama="danu")
```

**4.3 (prediksi output)**
```python
def hitung(a, b):
    return a + b, a * b

tambah, kali = hitung(3, 4)
print(tambah, kali)
```

**4.4 (prediksi output)** Kenapa hasilnya berbeda dari ekspektasi kebanyakan orang?
```python
angka = 10

def ubah():
    angka = 99
    print(angka)

ubah()
print(angka)
```

**4.5 (prediksi output)**
```python
def total(*args):
    hasil = 0
    for angka in args:
        hasil += angka
    return hasil

print(total(1, 2, 3))
print(total(5))
```

**4.6 (teori)** Apa arti type hinting pada function berikut?
```python
def hitung_bmi(berat: float, tinggi: float) -> float:
    ...
```

**4.7 (coding)** Buat function `hitung_diskon(harga: float, persen: float = 10) -> float`
yang mengembalikan harga setelah diskon. Panggil dengan keyword argument.

**4.8 (coding)** Buat function `rata_rata(*angka)` yang mengembalikan rata-rata
dari semua angka yang dikirim. Jika tidak ada angka, kembalikan `0`.

---

## Bagian 5 — Struktur Data (list / tuple / set / dict)

**5.1 (prediksi output)**
```python
angka = [10, 20, 30, 40, 50]
print(angka[0])
print(angka[-1])
print(angka[1:4])
```

**5.2 (prediksi output)**
```python
buah = ["apel", "jeruk"]

buah.append("mangga")
buah.insert(0, "pisang")
buah.remove("jeruk")
print(buah)
print(len(buah))
```

**5.3 (prediksi output)** Apa isi list setelah kode ini?
```python
nilai = [3, 1, 4, 1, 5]

nilai.sort()
print(nilai)

nilai_2 = [3, 1, 4]
print(sorted(nilai_2, reverse=True))
```

**5.4 (prediksi output)** Mana yang error? Jelaskan.
```python
tuple_a = (1, 2, 3)
tuple_a[0] = 99
```

**5.5 (prediksi output)**
```python
angka = {1, 2, 2, 3, 3, 3}
print(angka)

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a & b)
```

**5.6 (prediksi output)**
```python
mahasiswa = {"nama": "radit", "umur": 20}

print(mahasiswa["nama"])
print(mahasiswa.get("hobi", "tidak ada"))
mahasiswa["umur"] = 21
mahasiswa["kota"] = "bogor"
print(mahasiswa)
```

**5.7 (prediksi output)**
```python
for kunci, isi in mahasiswa.items():
    print(f"{kunci}: {isi}")
```
(diasumsikan `mahasiswa = {"nama": "radit", "umur": 21, "kota": "bogor"}`)

**5.8 (teori)** Sebutkan 3 perbedaan utama `list` vs `tuple` vs `set`.

**5.9 (coding)** Diberikan list:
```python
belanja = ["susu", "roti", "susu", "telur", "roti", "susu"]
```
Hitung berapa kali setiap item muncul menggunakan dict. Output:
```
susu : 3
roti : 2
telur : 1
```

**5.10 (coding)** Hapus semua angka duplikat dari list, pertahankan urutan,
tanpa pakai `set` (hint: buat list baru + cek `in`).

---

## Bagian 6 — String Manipulation

**6.1 (prediksi output)**
```python
kalimat = "belajar python itu menyenangkan"

print(kalimat[0])
print(kalimat[-1])
print(kalimat[0:7])
print(kalimat[::-1])
```

**6.2 (prediksi output)**
```python
teks = "  halo dunia  "

print(teks.strip())
print(teks.upper())
print(teks.title())
print(teks.replace("dunia", "python"))
```

**6.3 (prediksi output)**
```python
data = "radit,bogor,20"

hasil = data.split(",")
print(hasil)
print(" | ".join(hasil))
```

**6.4 (prediksi output)**
```python
kalimat = "python itu seru"

print(kalimat.count("u"))
print(kalimat.find("itu"))
print(kalimat.find("java"))
```

**6.5 (prediksi output)**
```python
nama = "radit"
umur = 20

print(f"nama saya {nama}, tahun depan umur saya {umur + 1}")
```

**6.6 (coding)** Cek apakah sebuah kata adalah palindrome (dibaca sama
dari depan dan belakang, contoh: "katak"). Abaikan huruf besar/kecil.

**6.7 (coding)** Balik urutan kata (bukan huruf) dalam sebuah kalimat.
Contoh: `"saya suka python"` → `"python suka saya"`.

**6.8 (coding — challenge)** Hitung jumlah huruf vokal dan konsonan
dalam kalimat input user (abaikan spasi dan angka).

---

## Bagian 7 — Error Handling

**7.1 (teori)** Apa perbedaan error saat *syntax error* vs error saat
*runtime*? Berikan contoh masing-masing.

**7.2 (prediksi output)** Program ini error atau tidak? Jika tidak, output-nya?
```python
try:
    angka = int("abc")
except ValueError:
    print("bukan angka")

print("lanjut")
```

**7.3 (prediksi output)** Urutkan output yang tercetak:
```python
try:
    print("A")
    hasil = 10 / 0
    print("B")
except ZeroDivisionError:
    print("C")
else:
    print("D")
finally:
    print("E")
```

**7.4 (teori)** Sebutkan nama error (exception class) yang muncul dari:
1. `int("halo")`
2. `[1, 2, 3][10]`
3. `{}["kunci"]`
4. `print(variable_belum_ada)`
5. `"a" + 1`
6. `10 / 0`

**7.5 (prediksi output)** Apa output program ini?
```python
data = {"nama": "radit"}

try:
    print(data["umur"])
except KeyError:
    print("kunci tidak ada")
except Exception:
    print("error umum")
```

**7.6 (coding)** Buat program input angka yang terus meminta input
sampai user memasukkan angka yang valid:
```
Masukkan angka: abc
Bukan angka, coba lagi!
Masukkan angka: 10
Angka valid: 10
```

**7.7 (coding)** Buat function `ambil_element(list_data, index)` yang
mengembalikan nilai pada index tersebut, atau string `"index tidak valid"`
jika terjadi `IndexError`. Manfaatkan `try-except`.

---

## Bagian 8 — File I/O

**8.1 (teori)** Apa perbedaan mode `"r"`, `"w"`, dan `"a"` saat membuka file?

**8.2 (teori)** Kenapa lebih baik pakai `with open(...)` dibanding
`open(...)` lalu `close()` manual?

**8.3 (prediksi output)** Misal file `catatan.txt` berisi 3 baris.
Apa output program ini dan kenapa bentuknya seperti itu?
```python
with open("catatan.txt", "r") as f:
    isi = f.readlines()
    print(isi)
```

**8.4 (prediksi output)** Setelah kode ini dijalankan, apa isi file `data.txt`?
```python
with open("data.txt", "w") as f:
    f.write("baris 1\n")
    f.write("baris 2\n")

with open("data.txt", "a") as f:
    f.write("baris 3\n")
```

**8.5 (coding)** Buat program yang:
1. Menulis 5 nama temanmu ke file `teman.txt` (satu nama per baris)
2. Membaca file tersebut dan mencetaknya dengan format: `1. nama`

**8.6 (coding — challenge)** Buat program "buku tamu": setiap dijalankan,
user diminta nama + pesan, lalu disimpan ke `buku_tamu.txt` dengan format:
```
[nama] : pesan
```
Semua entri lama tidak boleh hilang. Program selesai jika user mengetik `"exit"`.

---

# PROJECT NON-OOP

Kerjakan berurutan, masing-masing menantang kombinasi materi berbeda.
Semua procedural (function + loop), tanpa class.

---

## Project 1 — Password Generator & Validator (level: mudah-menengah)

Materi: string manipulation, function, random, error handling.

Fitur:
1. Function `generate_password(panjang: int) -> str`
   - Gabungan huruf besar, kecil, angka (import `random` + `string`)
   - Panjang minimal 8, jika kurang beri warning (bukan crash)
2. Function `cek_kekuatan(password: str) -> str`
   - "kuat": ada huruf besar + kecil + angka + simbol, panjang >= 12
   - "sedang": ada huruf + angka, panjang >= 8
   - "lemah": selain itu
3. Menu loop: user pilih (1) generate password (2) cek kekuatan password (3) keluar

---

## Project 2 — To-Do List CLI dengan Save/Load (level: menengah)

Materi: list, dict, function, loop, error handling, file I/O —
project ini merefresh hampir semua materimu.

Fitur:
1. Tambah tugas: simpan sebagai dict `{"judul": ..., "selesai": False}`
2. Lihat tugas: tampilkan dengan nomor + status `[x]` / `[ ]`
   (pakai `enumerate`!)
3. Tandai selesai
4. Hapus tugas
5. Auto-save ke `todo.txt` setiap ada perubahan (format bebas,
   misal: `judul|selesai` lalu di-parse dengan `split`)
6. Saat program dibuka, load file tersebut
   (tangani `FileNotFoundError` untuk pemakaian pertama)
7. Input menu tidak valid tidak boleh membuat program crash

---

## Project 3 — Aplikasi Kasir Toko (level: menantang, capstone)

Materi: semua yang di atas + structuring data yang lebih kompleks.

Spesifikasi:
1. Data produk disimpan dalam dict:
```python
produk = {
    "P001": {"nama": "beras 5kg", "harga": 65000},
    "P002": {"nama": "minyak 1L", "harga": 18000},
    "P003": {"nama": "gula 1kg", "harga": 15000},
}
```
2. Keranjang belanja: user input kode produk + jumlah,
   tampilkan subtotal tiap penambahan
3. Input kode yang tidak ada / jumlah bukan angka → error handling,
   program tetap jalan
4. Saat selesai (`selesai`), tampilkan struk rapi:
   ```
   ===== STRUK BELANJA =====
   beras 5kg      x2 = 130000
   gula 1kg       x1 =  15000
   -------------------------
   TOTAL               145000
   DISKON (10%)         14500
   TOTAL BAYAR         130500
   ```
5. Diskon: 10% jika total >= 100000
6. Struk tersimpan ke file `struk_{nomor}.txt`
   (nomor struk bertambah tiap transaksi)
7. Pecah program menjadi function yang rapi:
   `tampilkan_produk()`, `tambah_keranjang()`, `hitung_total()`,
   `cetak_struk()`, dan `main()` sebagai loop utama

Bonus: riwayat transaksi disimpan ke `riwayat.txt`,
dan menu admin untuk menambah produk baru.
