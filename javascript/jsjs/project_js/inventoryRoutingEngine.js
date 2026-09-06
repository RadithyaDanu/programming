/*
=========================================================
PEMELASAN LEVEL SENIOR: Inventory Routing Engine
=========================================================
*/

// DATA MENTAH: Daftar stok barang di dua gudang berbeda
const gudangPusat = [
  { sku: "ITEM-A", nama: "Mechanical Keyboard", stok: 10, beratKg: 1 },
  { sku: "ITEM-B", nama: "Gaming Monitor", stok: 2, beratKg: 5 },
  { sku: "ITEM-C", nama: "Mousepad XL", stok: 25, beratKg: 0.5 }
];

// Daftar pesanan masuk dari client (E-Commerce Order)
const daftarPesanan = [
  { sku: "ITEM-A", qtyDiminta: 3 },
  { sku: "ITEM-C", nama: "Mousepad XL", qtyDiminta: 30 }, // Minta lebih dari stok pusat (25)!
  { sku: "ITEM-B", nama: "Gaming Monitor", qtyDiminta: 3 }, // Stok pusat cuma 2, kurang 1!
  { sku: "ITEM-D", nama: "Unknown Item", qtyDiminta: 1 }   // Barang fiktif/tidak terdaftar!
];

let totalBarangTerkirim = 0;
let totalBeratPengiriman = 0;

console.log("=== MEMPROSES PENGIRIMAN PESANAN ===");

// AREA KERJA: Tulis perulangan for...of (atau nested loop/logika di dalamnya)
// ...

// ATURAN MAIN:
// 1. Validasi Barang Tidak Terdaftar:
//    Cek apakah SKU pesanan ada di dalam 'gudangPusat'. 
//    Jika barang TIDAK DITEMUKAN sama sekali di gudang, cetak: 
//    "ERROR 404: SKU [sku] tidak ditemukan di sistem!" lalu gunakan 'continue'.
for (let item of daftarPesanan) {
    let barangDitemukan = null;

    for (let barang of gudangPusat) {
        if (item.sku === barang.sku) {
            barangDitemukan = barang;
        }
    }

    if (barangDitemukan === null) {
        console.log(`ERROR 404: SKU ${item.sku} tidak ditemukan di sistem!`);
        continue;
    }

    if (item.qtyDiminta > barangDitemukan.stok) {
        console.log(`STOK HABIS: Gagal mengirim ${barangDitemukan.nama}, stok gudang tidak cukup.`);
        continue;
    }

    barangDitemukan.stok -= item.qtyDiminta;

    totalBarangTerkirim += item.qtyDiminta;
    totalBeratPengiriman += item.qtyDiminta * barangDitemukan.beratKg;

    if (totalBeratPengiriman >= 15) {
        console.log(`LIMIT KAPASITAS: Truk pengiriman penuh! Menghentikan proses sisa pesanan.`);
        break;
    }
}
// 2. Validasi & Pengurangan Stok Gudang:
//    Cek apakah 'qtyDiminta' LEBIH BESAR dari 'stok' gudang yang tersedia.
//    Jika stok tidak mencukupi, cetak: 
//    "STOK HABIS: Gagal mengirim [nama_barang], stok gudang tidak cukup." lalu gunakan 'continue'.
//    Jika stok mencukupi, KURANGI nilai 'stok' di dalam objek 'gudangPusat' dengan 'qtyDiminta'.

// 3. Kalkulasi Logistik:
//    Jika barang berhasil diproses (stok cukup & ada di gudang), 
//    tambahkan 'qtyDiminta' ke 'totalBarangTerkirim'.
//    Hitung total berat (qtyDiminta dikali beratKg barang tersebut) dan akumulasikan ke 'totalBeratPengiriman'.

// 4. Pembatasan Beban Server (Break System):
//    Jika total akumulasi 'totalBeratPengiriman' sudah MENCAWEI ATAU MELEBIHI 15 kg,
//    cetak: "LIMIT KAPASITAS: Truk pengiriman penuh! Menghentikan proses sisa pesanan." 
//    lalu hentikan seluruh perulangan menggunakan 'break'.


// HASIL AKHIR (Jangan ubah bagian ini)
console.log("===================================");
console.log(`Total Barang Berhasil Dikirim: ${totalBarangTerkirim} pcs`);
console.log(`Total Berat Pengiriman: ${totalBeratPengiriman} kg`);