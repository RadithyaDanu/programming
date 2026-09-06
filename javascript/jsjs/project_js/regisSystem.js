/*
=========================================================
PROJECT 1: User Registration System (In-Memory CRUD)
=========================================================
*/
const dbUsers = [
  { username: "pegawai1", email: "pegawai1@kantor.com" }
];

// FUNGSI 1: Mencari User
// Tugas: Lakukan perulangan ke 'dbUsers'. Jika email ditemukan, return Object user-nya. 
// Jika sampai perulangan selesai tidak ditemukan, return null.
function cariUser(email) {
    for (const user of dbUsers){
        if(user.email === email){
            return user;
        }
    }
    return null;
}

// FUNGSI 2: Mendaftar User Baru
// Tugas:
// 1. Panggil fungsi cariUser(email) di dalam fungsi ini dan simpan hasilnya di variabel.
// 2. Jika hasilnya BUKAN null (artinya email sudah terdaftar), return teks: "ERROR: Email [email] sudah digunakan!"
// 3. Jika null (email belum ada), masukkan object baru { username, email } ke dalam 'dbUsers' menggunakan dbUsers.push()
// 4. Return teks: "SUCCESS: User [username] berhasil didaftarkan!"
function daftarUser(username, email) {
    const result = cariUser(email)
    if (result !== null){
        return `ERROR: Email ${email} sudah digunakan!`
    }
    else if (result === null) {
        dbUsers.push({username, email})
        return `SUCCESS: User ${username} berhasil didaftarkan!`
    }
}

console.log("=== HASIL TESTING PROJECT 1 ===");
console.log(daftarUser("radit_dev", "radit@mail.com")); // Harus SUCCESS
console.log(daftarUser("hacker99", "pegawai1@kantor.com")); // Harus ERROR
console.log(daftarUser("guest123", "radit@mail.com")); // Harus ERROR
console.log("Isi Database Sekarang:", dbUsers);


// refactor function 2
function daftarUser(username, email) {
    const result = cariUser(email);
    
    // Guard Clause: Tolak jika user sudah ada
    if (result !== null) {
        return `ERROR: Email ${email} sudah digunakan!`;
    }
    
    // Jika kode sampai sini, pasti result === null
    dbUsers.push({ username, email });
    return `SUCCESS: User ${username} berhasil didaftarkan!`;
}

// kalo cuma 2 kondisi dan kondisinya pake return, better gausah ada else if 
// karena kalo return pertama accepted, program otoamtis berhenti
