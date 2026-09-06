const profil = {
    firstName : "Radithya",
    lastName : "Danutirta"
}

const result = "firstName" in profil;
console.log(`firstname apakah true : ${result}`);

if ("firstName" in profil) {
    console.log(`halo ${profil.firstName}`);
} else {
    console.log("atribut tidak ada di profil");
}

// mengecek apakah sebuah properti, atribut atau index ada pada object atau array
// namun hanya mengecek apakah ada atau tidak, tidak peduli isinya apa 
// meskipun data null atau undefined, maka tetap mencetak true
console.log("-----------------------------")
const salah = {
    nama : "radit",
    umur : null
}

const pembuktian = "umur" in salah;
console.log(pembuktian);
console.log(salah.umur);