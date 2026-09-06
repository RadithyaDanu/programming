// const person = {};
// const test = person.data.country;
// //error dan program berhenti disini

// console.log(test);
// console.log("o")

//optional chaining mengamankan saat kita akses objek yang memiliki data nullish (null/undefined)
// supaya program tetap berjalan dan mengamankan kita dari data nullish, bisa pakai if namun ribet
/*
const data = {};
let nyoba;

if (data.alamat !== undefined && data.alamat !== null){
    nyoba = data.alamat.negara;
};

console.log(nyoba);
 */
// nah dengan ini, program tetap berjalan dan mengembalikan nilai undefined pada output
// cara lebih mudah adalah menggunakan optional chaining operator

let person = {};
console.log(person?.alamat?.negara);
