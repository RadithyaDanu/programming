let result = 1 + 2; // disini result langsung simpen value 3,
// jadi ketika result diubah, value 3 tidak akan berubah, karena result sudah menyimpan value 3
console.log("hasil dari 1 + 2 = " + result);
let originalResult = result;

result = result - 1; // disini result nyimpen value 3 dan  result diubah menjadi 2, tapi originalResult tetap 3
console.log("hasil dari " + originalResult + " - 1 = " + result);
originalResult = result;

result = result * 2;
console.log("hasil dari " + originalResult + " x 2 = " + result);

// opeartor augmented assignments
console.log("AUGMENTED ASSIGNMENTS");
let hasil = 1 + 2; // disini hasil langsung simpen value 3,
// jadi ketika hasil diubah, value 3 tidak akan berubah, karena hasil sudah menyimpan value 3
console.log("hasil dari 1 + 2 = " + hasil);
let originalResult = hasil;

hasil -= 1; // disini hasil nyimpen value 3 dan  result diubah menjadi 2, tapi originalResult tetap 3
console.log("hasil dari " + originalResult + " - 1 = " + hasil);
originalResult = hasil;

hasil *= 2;
console.log("hasil dari " + originalResult + " x 2 = " + hasil);

// operator unary
// operator yang biasanya membutuhkan 1 data
let result = +1; // disini result langsung simpen value 1
console.log("<p>" + result + "</p>");

result--; // result kena decrement jadi berkurang 1, result sekarang 0
console.log("<p>" + result + "</p>");

result++; // result kena increment jadi bertambah 1, result sekarang 1
console.log("<p>" + result + "</p>");

result = -result; // result diubah jadi negiatf, maka result sekarang -1
console.log("<p>" + result + "</p>");