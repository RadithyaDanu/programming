// break = stop perulangan saat ini tanpa mengecek kondisi lagi
// continue = stop perulangan saat ini dan melanjutkan ke perulangan selanjutnya

let counter = 1;
while (true) {
    console.log(`ini perulangan ke ${counter}`)
    counter++;

    if (counter > 10){
        break;
    }
}

// while true berarti akan selalu melakukan perulangan
// tanpa break maka perulangan akan berlanjut terus

// continue

for (let i = 1; i <= 100; i++){
    if (i % 2 === 0) {
        continue;
    } console.log(`bilangan ganjil 1-100 : ${i}`)
} 
// penjelasan kode
// disini kita pengen mencetak angka ganjil dari 1 sampai 100
// bilangan ganjil jika dibagi 2 akan menghasilkan 1 jika di modulus
// jadi jika bilangan habis di bagi 2(genap)
// maka continue (melanjutkan perulangan tanpa mengeksekusi console.log)
// jadi saat bertemu bilangan genap, perulangan akan di stop dan lanjut ke bilangan selanjutnya
// saat stop, increment akan dieksekusi dulu baru lanjut ke loop