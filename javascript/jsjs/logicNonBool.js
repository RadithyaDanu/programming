// operator logika di non boolean

console.log("hello" || "");
console.log("" || []);
console.log( "0" || "NOL");
console.log("" || 0);
console.log(null || "null");
console.log(undefined || null); 

/*
operator and dan or pada js tidak hanya untuk 2 data boolean
tapi juga bisa pake falsy dan truthy
1. operator or ||
    membaca program dari kiri ke kanan, mengambil nilai true/truthy pertama
    jika tidak ada nilai true, maka data paling terakhir atau kanan yang diambil
*/

// dipake saat kapan?
const person = {
    firstName :"",
    lastName : "danutirta"
};

const name = person.firstName || person.lastName;

// jika first name null atau falsy, maka lastname akan diambil, namun jika keduanya null maka lastname diambil
console.log(name);


// operator and &&
/*
mengambil nilai false pertama, kebalikan dari or
misal gaada satupun nilai false, maka ambil paling kanan/ terakhir
*/

console.log("hello" && "");
console.log("" && {});
console.log({} && "halo");