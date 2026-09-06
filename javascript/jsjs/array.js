let nama = ["radithya", "danutirta", "radithya danutirta"];
console.log(nama);

let campur = ["radithya", 21, true, {nama: "radithya"}, [1,2,3]]
console.log(campur);
console.log(`ini data index ke 1 = ${campur[1]}`);

console.table(campur); // menampilkan array dalam bentuk tabel
// cara akses array pake index. index dimulai dari 0, data pertama ada di index 0
// cara menambahkan data ke array bisa pake push, unshift, splice, dll
// tipe data pada array bisa beda beda, misal string, number, bool, object, array, funct, dll
// array bisa diubah isinya, misal data index ke 1 diubah dari 21 menjadi 22
// nambahin data berarti ada di posisi terakhir


// nambah array
const nama2 = [];
nama2.push("radithya");
nama2.push("danutirta", 21);
console.log(`ini isi nambah array nama2 = ${nama2}`);
console.log(nama2);


console.table(nama2); // menampilkan array dalam bentuk tabel


// operasi array
const ubah = [];
ubah.push("radithya", "danutirta", "unpam");
ubah[0];
ubah[0] = "radithya danutirta"; // mengubah data index ke 0
ubah[1] = "danu";
ubah.length;

console.log(ubah);
console.log(`panjang array ubah = ${ubah.length}`);

delete ubah[0];
console.log(`disini array ubah yang telah dihapus index ke 0 nya 'radithya danutirta' = ${ubah}`);