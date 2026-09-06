//menurunkan scope data
// mengakses properti dari data tanpa menyebutkna data
// biasanya kita menggunakan person.firstName untuk mendapatkan data
// contoh

const person = {
    firstName : "radithya",
    middleName : "danu",
    lastName : "tirta"
};
console.log(person.firstName);

//itu basic
// dibawha ini penggunaan with statement

with(person) {
    console.log(firstName);
    console.log(middleName);
    console.log(lastName);
}

// jadi kita memanggil person terlebih dahulu 