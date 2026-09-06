// for loop
// merupakan salah satu perulangan di js
// selalu melakukan perulangan di dalam blok kode for
// for loop memiliki kode seperti berikut :
/* for (init statment; kondisi; post statement) {
        // blok kode
    }
init, kondisi dan post statement tidak wajib diisi, jika kondisi tidak diisi maka selalu bernilai true.
- init selalu dieksekusi diawal
- kondisi selalu dieksekusi sampai kondisi bernilai true
- post dieksekusi diakhir perulangan, jadi setelah kondisi true lalu post lalu kondisi dan post, begitu seterusnya

for (; ;) {
    console.log("alert")
}
*/
// infinite loop

// 1. for loop dengan kondisi
let counter = 1;
for (;counter <= 10;) {
    console.log(`perulangan ke ${counter}`)
    counter++; // diakhir dikasih increment, supaya nilainya bertambah, jika tidak diberikan increment
    // maka kondisi akan selalu true yang menyebabkan terjadinya infinite loop
}

// 2. for loop dengan init statement
// kita memasukan variabel counter ke dalam loop, karena init statement dieksekusi sekali saja
for (counter2 = 1; counter2 <= 10;){
    console.log(`loop dengan init dan kondisi ke ${counter2}`)
    counter2++;
}

// 3. for loop dengan pos statment
// masukin increment ke dalam post statement
for (counter3 = 1; counter3 <= 10; counter3++){
    console.log(`loop dengan init, kondisi, dan post ke ${counter3}`);
}