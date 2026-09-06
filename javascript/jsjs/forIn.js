// perulangan yang digunakan untuk mengiterasi seluurh data properti di object atau index di array
// ga rekom dipake ke array

const person= {
    firstName : "radithya",
    middleName : "danu",
    lastName : "tirta"
}

for (const property in person) {
    console.log(`properti ${property} : ${person[property]}`)
}

// kalo bikin di array, dia akan nangkep indexnya

const ar = ["radithya", "danutirta"]
for (const pro in ar){
    console.log(`${pro} : ${ar[pro]}`)
}