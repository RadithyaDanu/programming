/*
=========================================================
PROJECT 2 (EXTREME): E-Commerce Transaction Engine
=========================================================
*/

// Tabel Produk Database
const dbProduk = [
  { sku: "BRG-01", nama: "Sepatu Lari", harga: 250000, stok: 5 },
  { sku: "BRG-02", nama: "Kaus Polos", harga: 50000, stok: 10 },
  { sku: "BRG-03", nama: "Topi Baseball", harga: 35000, stok: 0 }
];

// FUNGSI BANTUAN 1: Ambil Data Produk
// Tugas: Return object produk berdasarkan SKU. Jika tidak ketemu, return null.
function getProduk(sku) {
  for (const items of dbProduk){
    if (sku === items.sku){
        return items;
    }
  }
  return null;
}

// FUNGSI BANTUAN 2: Hitung Pajak PPN 11%
// Tugas: Menerima parameter total harga, return hasil pajaknya (11% dari total harga).
function hitungPPN(totalHarga) {
  let pajak = 0.11;
  let hasil = totalHarga * pajak
  return hasil;
}

// FUNGSI UTAMA: Proses Pesanan (Controller)
// Menerima parameter berupa 'keranjang' (Array of Objects dari request client)
function prosesPesanan(keranjang) {
  let subtotal = 0;
  let barangBerhasil = [];
  let barangGagal = [];

  // TUGAS LOGIKA:
  // 1. Lakukan perulangan untuk menelusuri array 'keranjang'
  // 2. Di dalam perulangan, panggil getProduk(item.sku) untuk mencari data aslinya.
  // 3. Jika produk return null ATAU stoknya KURANG dari 'item.qty',
  //  masukkan nama pesanan ke array 'barangGagal' dengan metode push().
  // 4. Jika valid dan stok cukup: 
  //    - Kurangi stok asli di database.
  //    - Tambahkan harga * qty ke 'subtotal'.
  //    - Masukkan nama produk ke array 'barangBerhasil' menggunakan push().

  // (Tulis logika perulanganmu di sini...)
  for (const items of keranjang){
    const dataRill = getProduk(items.sku)
    if (dataRill.sku === null || dataRill.stok < items.qty){
        barangGagal.push(dataRill.nama);
    } else {
    dataRill.stok -= items.qty;
    subtotal += dataRill.harga * items.qty;
    barangBerhasil.push(dataRill.nama);
    }
  }
  // 5. Panggil fungsi hitungPPN(subtotal) dan simpan hasilnya.
  let pajak = hitungPPN(subtotal);

  // 6. Return sebuah Object (Response API) yang berisi rincian transaksi:
  return {
    status: "PROSES SELESAI",
    detail_tagihan: {
      subtotal: subtotal,
      pajak_ppn: pajak,
      total_bayar: subtotal + pajak
    },
    laporan_pengiriman: {
      sukses: barangBerhasil,
      gagal: barangGagal
    }
  };
}



// --- AREA TESTING (Jangan ubah bagian ini) ---
const requestKeranjang = [
  { sku: "BRG-01", qty: 2 }, // Stok 5, aman. Subtotal: 500.000
  { sku: "BRG-03", qty: 1 }, // Stok 0, gagal!
  { sku: "BRG-02", qty: 15 } // Minta 15, stok 10, gagal!
];

console.log("=== INVOICE TRANSAKSI ===");
const invoice = prosesPesanan(requestKeranjang);
console.log(invoice);