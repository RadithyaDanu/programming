const num = 5;
const str = "5";
const float = "5.5";

const convertStrToNum = parseInt(str);
const convertStrToFloat = parseFloat(float);
const convertStrToNum2 = Number(str);
const convertNumToStr = num.toString();
const convertFloatToStr = float.toString();

const penjumlahan1 = convertStrToNum + num; // 5 + 5 = 10
const penjumlahan2 = convertStrToFloat + num; // 5.5 + 5 = 10.5
const penjumlahan3 = convertNumToStr + num;


console.log(`
        hasil str to num = ${convertStrToNum} 
        hasil str to float = ${convertStrToFloat} 
        hasil str to num (Number) = ${convertStrToNum2} 
        hasil num to str = ${convertNumToStr} 
        hasil float to str = ${convertFloatToStr}`);

//konversi yang bukan angka akan menghasilkan NaN (not a number)