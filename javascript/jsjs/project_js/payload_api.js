/*
=========================================================
MINI PROJECT: Simulasi Validasi Payload API (Middleware)
=========================================================
*/

// 1. PERSIAPAN DATA MENTAH (Mock Request)
// Object di bawah ini mensimulasikan request.body dari client ke server backend.
/*
const payload = {
  username: "admin_bendi",
  email: "admin@bendi.com",
  umur: 16,
  status_pembayaran: "lunas", // Sengaja dibuat string untuk menjebak
  is_active: true
};
*/

// 2. SKENARIO VALIDASI (Tugas Utama)
// Gunakan struktur percabangan (if, else if, else) untuk memvalidasi 'payload' di atas.

// Aturan A: Validasi Umur
// Cek apakah 'umur' di bawah 18. 
// Jika ya, cetak: "Akses ditolak: Pengguna harus berusia 18 tahun ke atas."

// Aturan B: Validasi Status Pembayaran
// Cek apakah 'status_pembayaran' benar-benar bertipe boolean dengan nilai 'true'.
// Jika nilainya bukan boolean true (misal string "lunas"), cetak: "Error: tipe data status_pembayaran tidak valid."

// Aturan C: Validasi Akun Aktif
// Jika 'is_active' bernilai false, cetak: "Peringatan: Akun sedang dibekukan."

// Aturan D: Lolos Validasi
// Jika semua kondisi A, B, dan C terpenuhi secara valid (tidak memicu error),
// cetak: "Payload valid! Melanjutkan proses penyimpanan ke database..."

// 3. AREA KERJA (Tulis kode logika If/Else kamu di bawah baris ini)
// ...

const payload = {
  username: "radit",
  email: "admin@radit.com",
  umur: 21,
  status_pembayaran: true,
  is_active: true
};

if (payload.umur < 18) {
    console.log("Akses ditolak: Pengguna harus berusia 18 tahun ke atas.");
} else if (payload.status_pembayaran !== true) {
    console.log("Error: tipe data status_pembayaran tidak valid.");
} else if (payload.is_active === false) {
    console.log("Peringatan: Akun sedang dibekukan");
} else {
    console.log("Payload valid! Melanjutkan proses penyimpanan ke database...");
}


