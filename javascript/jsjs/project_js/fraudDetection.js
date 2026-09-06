/*
=========================================================
MINI PROJECT 2: Aggregasi Laporan Transaksi & Deteksi Fraud
=========================================================
*/

// 1. DATA MENTAH (Mock Database Query)
// Array ini mensimulasikan hasil tarikan baris data dari database.
const laporanTransaksi = [
  { id: "TRX-001", status: "berhasil", nominal: 250000 },
  { id: "TRX-002", status: "pending", nominal: 150000 },
  { id: "TRX-003", status: "berhasil", nominal: 50000 },
  { id: "TRX-004", status: "gagal", nominal: 75000 },
  { id: "TRX-005", status: "fraud", nominal: 5000000 }, // Transaksi anomali!
  { id: "TRX-006", status: "berhasil", nominal: 120000 }
];

let totalPendapatan = 0;
console.log(` testing : ${laporanTransaksi[1].id}`)
// 2. SKENARIO PEMROSESAN 
// Gunakan perulangan (For Loop) untuk menelusuri array 'laporanTransaksi'.

// Aturan A: Abaikan Data (Continue)
// Di dalam loop, cek jika status transaksi "pending" atau "gagal".
// Jika ya, gunakan perintah 'continue' agar program langsung melompat mengecek transaksi berikutnya.

// Aturan B: Hentikan Sistem (Break)
// Jika menemukan status "fraud", cetak pesan error: 
// "Sistem dihentikan: Terdeteksi transaksi fraud pada ID [id_transaksi]"
// Lalu gunakan perintah 'break' untuk menghentikan seluruh perulangan saat itu juga.

// Aturan C: Akumulasi Pendapatan
// Jika statusnya "berhasil", tambahkan nilai 'nominal' ke variabel 'totalPendapatan'.

// 3. AREA KERJA (Tulis perulangan kamu di bawah baris ini)
// ...
for (let i = 0; i < laporanTransaksi.length; i++) {
    if (laporanTransaksi[i].status === "pending" || laporanTransaksi[i].status === "gagal"){
        continue;
    }
    else if (laporanTransaksi[i].status === "fraud") {
        console.log(`Sistem dihentikan: Terdeteksi transaksi fraud pada ID ${laporanTransaksi[i].id}`)
        break;
    }
    else if (laporanTransaksi[i].status === "berhasil") {
        totalPendapatan += laporanTransaksi[i].nominal
    }
}

console.log("Total Pendapatan Bersih: Rp " + totalPendapatan)


// 4. HASIL AKHIR
// Di luar/setelah blok perulangan, cetak hasil perhitungannya:
// console.log("Total Pendapatan Bersih: Rp " + totalPendapatan);