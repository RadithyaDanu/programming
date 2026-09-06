// merepresentasikan data yang belum diberikan

let name;
console.log(name);
//bakal keluar undefined

// misal bikin array terus pengen akses index ke 3 sedangkan kita cuma punya sampe index 2
// outputnya bakal undefined

const aray = ["ayam", "goreng", "dimsum mentai"]
console.log(`ini milih index ke 3 pasti undefined : ${aray[3]}`);

if (aray[3] === undefined) {
    console.log("undefined");
} else {
    console.log("udah bener");
}

let person = {};
person["name"] = "radithya"

if (person.name === undefined) {
    console.log("undefined");
} else {
    console.log("udah bener");
}