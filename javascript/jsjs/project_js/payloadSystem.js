/*
=========================================================
MINI PROJECT 3: Validasi & Kalkulasi Keranjang Belanja
=========================================================
*/

// DATA MENTAH (Simulasi payload dari keranjang belanja user)
const keranjang = [
  { id: "P001", nama: "Laptop JS", harga: 10000000, qty: 1, kategori: "Elektronik", stok: 5 },
  { id: "P002", nama: "Mouse Wireless", harga: 300000, qty: 10, kategori: "Elektronik", stok: 5 }, // qty melebihi stok!
  { id: "P003", nama: "Buku Catatan", harga: 50000, qty: 3, kategori: "ATK", stok: 100 },
  { id: "P004", nama: "Keyboard Hacker", harga: -150000, qty: 1, kategori: "Elektronik", stok: 10 }, // Anomali harga minus!
  { id: "P005", nama: "Flashdisk 32GB", harga: 100000, qty: 2, kategori: "Elektronik", stok: 20 }
];

let totalBayar = 0;
let totalBarangBerhasil = 0;
let totalBarangGagal = 0;

console.log("=== MEMULAI PROSES CHECKOUT ===");

// AREA KERJA (Tulis perulangan kamu di bawah baris ini)
// ...

for (const trx of keranjang){
    if (trx.harga < 0){
        console.log(`SECURITY ALERT: Harga invalid pada barang ${trx.nama}!`)
        totalBarangGagal += 1
        break;
    }
    else if (trx.qty > trx.stok) {
        console.log(`STOK KURANG: ${trx.nama} gagal diproses.`)
        continue;
    }

    let subtotal = trx.harga * trx.qty
    if (trx.kategori === "Elektronik"){
        subtotal = subtotal * 0.90;
    }

    totalBayar += subtotal;
    totalBarangBerhasil += 1;
}
// Aturan 1 - Keamanan Sistem (Break):
// Cek jika 'harga' item kurang dari 0 (minus). 
// Jika iya, cetak "SECURITY ALERT: Harga invalid pada barang [nama]!" lalu hentikan seluruh perulangan (break).

// Aturan 2 - Validasi Stok (Continue):
// Cek jika jumlah beli ('qty') LEBIH BESAR dari 'stok'.
// Jika iya, cetak "STOK KURANG: [nama] gagal diproses." lalu lewati item tersebut (continue).

// Aturan 3 - Kalkulasi Subtotal & Diskon:
// Hitung subtotal sementara: harga dikali qty.
// Lalu, jika 'kategori' barang tersebut adalah "Elektronik", berikan diskon 10% pada subtotalnya.
// (Gunakan logika if, jika elektronik maka subtotal dikurangi 10% dari subtotal).

// Aturan 4 - Akumulasi Final:
// Tambahkan subtotal akhir (setelah diskon jika ada) ke dalam variabel 'totalBayar'.
// Jangan lupa tambahkan variabel 'totalBarangBerhasil' dengan 1 setiap kali ada barang yang berhasil diproses.



// HASIL AKHIR (Jangan ubah bagian ini)
console.log("===============================");
console.log(`Total Item Berhasil Diproses: ${totalBarangBerhasil} item`);
console.log(`Total Yang Harus Dibayar: Rp ${totalBayar}`);
console.log(`barang gagal = ${totalBarangGagal}`);