const examValue = 90;

if (examValue > 90) {
    console.log("anda lulus dengan nilai A");
} else if (examValue > 80) {
    console.log("anda lulus dengan nilai B");
} else {
    console.log("anda ga lulus");
}

// percabangan mengeksekusi kode dari atas ke bawah
// jika kondisi pertama sudah terpenuhi, maka kondisi bawah dicuekin

let age = 18;
let result = age > 18 ? "cukup umur" : "tidak cukup umur";
console.log(result);