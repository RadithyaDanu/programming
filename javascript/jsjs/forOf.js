// for in kan digunakan untuk mengiterasi property
// for of digunakan untuk mengiterasi terhadap isi value dari iterable object, sperti array, string, dll
// for of tidak bisa digunakan di object karena object bukan iterable

// for of di array

const contoh1 = ["pisang", "mangga", "jeruk", "semangka", "buah naga"]

for (const buah of contoh1){
    console.log(buah)
}
// otomatis akan tercetak vlue dari contoh1
// bisa juga digunakan untuk array yang didalamnya terdapat object

const gudangPusat = [
  { sku: "ITEM-A", nama: "Mechanical Keyboard", stok: 10, beratKg: 1 },
  { sku: "ITEM-B", nama: "Gaming Monitor", stok: 2, beratKg: 5 },
  { sku: "ITEM-C", nama: "Mousepad XL", stok: 25, beratKg: 0.5 }
];

for (const item of gudangPusat){
    console.log(item.sku, item.nama)
}

const nama  = "radithya"
for (const names of nama){
    console.log(names);
}