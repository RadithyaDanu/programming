const orang = {};

// nambah data
orang["nama"] = "radithya";
orang["umur"] = 21;
orang["alamat"] = "jakarta";

console.table(orang);

delete orang["umur"];
console.table(orang);

orang["umur"] = 20;
console.table(orang);

const perkenalan = {
    "nama lengkap" : "radithya danutirta",
    umur : 21,
    hobi : ["membaca", "menulis", "bermain game"]
}
console.table(perkenalan);

console.log(perkenalan["hobi"][1]);
perkenalan["hobi"][1] = "tidur";
console.log(perkenalan["hobi"]);
// object bisa dimasukin array, array bisa dimasukin object, object bisa dimasukin object,
//  object bisa dimasukin function, function bisa dimasukin object, function bisa dimasukin array, 
// array bisa dimasukin function
// cara aksesnya pake kotak dan indexnya, bisa pake dot juga, tapi kalo pake dot ga bisa pake spasi, 
// kalo pake kotak bisa pake spasi
console.log(perkenalan.hobi[2]);

//akses property object
console.log(`nama lengkapnya adalah ${perkenalan["nama lengkap"]}`)
console.log(`umur saya adalah ${perkenalan.umur}`);
console.log(`hobi saya adalah ${perkenalan.hobi}`);
