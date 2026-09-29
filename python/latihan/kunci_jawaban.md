# Kunci Jawaban — Soal Recall Python

Buka file ini HANYA setelah menjawab. Untuk soal prediksi output,
jalankan kodenya juga untuk verifikasi.

---

## Bagian 1 — Operator

**1.1** `/` = pembagian biasa (hasil float), `//` = pembagian bulat
(floor division, buang desimal), `%` = sisa bagi (modulo).
`10 / 3 = 3.333...`, `10 // 3 = 3`, `10 % 3 = 1`.

**1.2**
```
3.3333333333333335
3
1
8
```

**1.3** `16` (5+3=8, lalu 8*2=16).

**1.4**
```
True
False
False
False
True
```
Catatan: `5 == "5"` False karena beda tipe; `3 > 2 > 1` itu
`3 > 2 and 2 > 1` → True (chained comparison).

**1.5** Error `TypeError`, karena string tidak bisa dijumlahkan dengan int.
Perbaiki: `"10" + str(5)` → `"105"` (string concat) atau
`int("10") + 5` → `15` (penjumlahan angka).

---

## Bagian 2 — Kontrol Alur

**2.1** `B` (75 >= 70 tapi < 90).

**2.2** `buat ktp dulu` (nested if: umur cukup tapi punya_ktp False).

**2.3** `awal pekan` (pattern `|` berarti "atau").

**2.4** Contoh jawaban:
```python
bulan = int(input("masukkan bulan (1-12): "))

match bulan:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 hari")
    case 4 | 6 | 9 | 11:
        print("30 hari")
    case 2:
        print("28 hari")
    case _:
        print("bulan tidak valid")
```

**2.5** Contoh jawaban:
```python
tahun = int(input("tahun: "))

if (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0:
    print("kabisat")
else:
    print("bukan kabisat")
```

---

## Bagian 3 — Perulangan

**3.1**
```
1
4
9
16
25
```

**3.2** 4 kali. i = 0, 3, 6, 9 → 4 iterasi (saat i=12 loop berhenti).

**3.3**
```
0
1
2
selesai
```
`continue` melewati i=3, `break` berhenti di i=4 sebelum print.

**3.4** `loop selesai tanpa break`. Blok `else` pada for hanya jalan
jika loop selesai tanpa `break`.

**3.5**
```
1. apel
2. jeruk
3. mangga
```

**3.6**
```
*
**
***
```

**3.7** Contoh jawaban:
```python
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
```

**3.8** Contoh jawaban:
```python
n = int(input("angka: "))
hasil = 1
i = 1
while i <= n:
    hasil *= i
    i += 1
print(f"{n}! = {hasil}")
```

**3.9** Contoh jawaban:
```python
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

**3.10** Contoh jawaban:
```python
n = int(input("n: "))

for angka in range(2, n + 1):
    for i in range(2, angka):
        if angka % i == 0:
            break
    else:
        print(angka)
```
Kunci: `for-else` — else jalan jika tidak ada break (artinya prima).

---

## Bagian 4 — Function

**4.1** `print()` hanya menampilkan ke layar, tidak mengembalikan nilai
(hasilnya `None`). `return` mengirim nilai keluar dari function agar
bisa disimpan di variabel / dipakai di hitungan lain.

**4.2**
```
halo tamu
halo radit
halo danu
```

**4.3** `7 12` (multiple return value → tuple unpacking).

**4.4**
```
99
10
```
`angka = 99` di dalam function membuat *local variable* baru,
tidak mengubah global `angka`.

**4.5** `6` dan `5` (args dikumpulkan jadi tuple).

**4.6** Parameter `berat` dan `tinggi` seharusnya float, dan function
akan mengembalikan float. Type hinting hanyalah petunjuk (tidak
memaksa saat runtime).

**4.7** Contoh jawaban:
```python
def hitung_diskon(harga: float, persen: float = 10) -> float:
    return harga - (harga * persen / 100)

print(hitung_diskon(100000))                     # 90000.0
print(hitung_diskon(harga=50000, persen=20))     # 40000.0
```

**4.8** Contoh jawaban:
```python
def rata_rata(*angka):
    if len(angka) == 0:
        return 0
    return sum(angka) / len(angka)
```

---

## Bagian 5 — Struktur Data

**5.1**
```
10
50
[20, 30, 40]
```

**5.2**
```
['pisang', 'apel', 'mangga']
3
```

**5.3**
```
[1, 1, 3, 4, 5]
[4, 3, 1]
```

**5.4** Error `TypeError: 'tuple' object does not support item assignment`
— tuple immutable (tidak bisa diubah setelah dibuat).

**5.5**
```
{1, 2, 3}
{1, 2, 3, 4, 5}
{3}
```
Set otomatis hapus duplikat; `|` union, `&` intersection.

**5.6**
```
radit
tidak ada
{'nama': 'radit', 'umur': 21, 'kota': 'bogor'}
```

**5.7**
```
nama: radit
umur: 21
kota: bogor
```

**5.8** Contoh jawaban:
- list: mutable, pakai `[]`, urutan terjaga, izinkan duplikat
- tuple: immutable, pakai `()`, urutan terjaga, izinkan duplikat
- set: mutable, pakai `{}`, tanpa urutan/index, duplikat otomatis hilang

**5.9** Contoh jawaban:
```python
belanja = ["susu", "roti", "susu", "telur", "roti", "susu"]
hitungan = {}

for item in belanja:
    hitungan[item] = hitungan.get(item, 0) + 1

for item, jumlah in hitungan.items():
    print(f"{item} : {jumlah}")
```

**5.10** Contoh jawaban:
```python
data = [1, 3, 1, 2, 3, 5, 2]
hasil = []

for angka in data:
    if angka not in hasil:
        hasil.append(angka)

print(hasil)  # [1, 3, 2, 5]
```

---

## Bagian 6 — String

**6.1**
```
b
g
belajar
gnadneganysnem uti nohtyp rajaleb
```

**6.2**
```
halo dunia
  HALO DUNIA  
  Halo Dunia  
  halo python  
```
Catatan: `upper()`, `title()`, `replace()` tidak menghapus spasi —
hanya `strip()` yang menghapusnya.

**6.3**
```
['radit', 'bogor', '20']
radit | bogor | 20
```

**6.4**
```
2
7
-1
```
"python itu seru": ada 'u' di "itu" dan "seru" = 2.
`find` mengembalikan -1 jika tidak ditemukan (tidak error).

**6.5** `nama saya radit, tahun depan umur saya 21`

**6.6** Contoh jawaban:
```python
kata = input("kata: ").lower()
if kata == kata[::-1]:
    print("palindrome")
else:
    print("bukan palindrome")
```

**6.7** Contoh jawaban:
```python
kalimat = "saya suka python"
kata_list = kalimat.split()
print(" ".join(kata_list[::-1]))        # python suka saya
# atau: print(" ".join(reversed(kata_list)))
```

**6.8** Contoh jawaban:
```python
kalimat = input("kalimat: ").lower()
vokal = "aeiou"
jumlah_vokal = 0
jumlah_konsonan = 0

for huruf in kalimat:
    if huruf.isalpha():
        if huruf in vokal:
            jumlah_vokal += 1
        else:
            jumlah_konsonan += 1

print(f"vokal: {jumlah_vokal}, konsonan: {jumlah_konsonan}")
```

---

## Bagian 7 — Error Handling

**7.1** Syntax error terdeteksi sebelum program berjalan (salah tulis,
misal kurang `:` atau tutup kurung) — program tidak jalan sama sekali.
Runtime error (exception) terjadi saat program berjalan, misal
pembagian nol atau index di luar batas — program berhenti di titik itu.

**7.2** Tidak error. Output:
```
bukan angka
lanjut
```
`int("abc")` memicu ValueError yang ditangkap except.

**7.3**
```
A
C
E
```
B tidak tercetak (baris error), D tidak jalan karena else hanya
jalan jika tidak ada error. Finally selalu jalan.

**7.4**
1. `ValueError`
2. `IndexError`
3. `KeyError`
4. `NameError`
5. `TypeError`
6. `ZeroDivisionError`

**7.5** `kunci tidak ada` — KeyError ditangkap handler pertama yang cocok
(Python cek urutan dari atas).

**7.6** Contoh jawaban:
```python
while True:
    masukan = input("Masukkan angka: ")
    try:
        angka = int(masukan)
        print(f"Angka valid: {angka}")
        break
    except ValueError:
        print("Bukan angka, coba lagi!")
```

**7.7** Contoh jawaban:
```python
def ambil_element(list_data, index):
    try:
        return list_data[index]
    except IndexError:
        return "index tidak valid"

print(ambil_element([10, 20, 30], 1))   # 20
print(ambil_element([10, 20, 30], 10))  # index tidak valid
```

---

## Bagian 8 — File I/O

**8.1** `"r"` = read (file harus ada, error jika tidak), `"w"` = write
(buat baru / TIMPA isi lama), `"a"` = append (tambah di akhir, isi lama aman).

**8.2** `with` otomatis menutup file walau terjadi error di tengah,
kodenya lebih ringkas, dan tidak ada risiko lupa `close()`.

**8.3** List berisi 3 string, contoh:
```
['baris pertama\n', 'baris kedua\n', 'baris ketiga\n']
```
`readlines()` mengembalikan list, dan karakter `\n` ikut di setiap elemen
(kecuali baris terakhir). Bersihkan dengan `.strip()` saat diproses.

**8.4** 3 baris:
```
baris 1
baris 2
baris 3
```
Mode `"w"` menimpa (baris 1 & 2 ditulis ulang), `"a"` menambah baris 3.

**8.5** Contoh jawaban:
```python
# 1. tulis
with open("teman.txt", "w") as f:
    for i in range(5):
        nama = input(f"nama teman {i + 1}: ")
        f.write(nama + "\n")

# 2. baca & tampilkan
with open("teman.txt", "r") as f:
    for nomor, baris in enumerate(f, start=1):
        print(f"{nomor}. {baris.strip()}")
```

**8.6** Contoh jawaban:
```python
while True:
    nama = input("nama (exit untuk selesai): ")
    if nama == "exit":
        break
    pesan = input("pesan: ")
    with open("buku_tamu.txt", "a") as f:
        f.write(f"[{nama}] : {pesan}\n")

print("terima kasih")
```
Kunci: gunakan mode `"a"` agar entri lama tidak hilang.

---

## Project — petunjuk pemeriksaan mandiri

Karena jawaban project bersifat terbuka, periksa dengan checklist:

**Password Generator**: password hasil generate lolos cek "kuat"?
Input panjang 3 tidak membuat crash? Menu invalid tidak crash?

**To-Do List**: setelah ditutup lalu dibuka lagi, apakah data bertahan?
`FileNotFoundError` saat pertama kali ditangani? Tugas selesai
tampil `[x]`? Input menu salah tidak crash?

**Kasir**: kode produk salah → pesan error + program lanjut?
Jumlah `abc` → tidak crash? Diskon muncul saat total >= 100000?
File struk benar terbuat dan nomornya bertambah? Struk rapi lurus
(pakai f-string alignment, mis. `f"{nama:<15}"`)?

Jika ada yang tidak lolos, buka lagi catatan materimu di folder
`pzn/` — semua bahan jawabannya ada di sana.
