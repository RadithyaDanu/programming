// string template
const nama = "Radithya Danutirta";
const umur = 21;
const tinggi = 175;
const result = `nama saya = ${nama} \numur saya = ${umur} \ntinggi saya = ${tinggi}`;
console.log(result);

const nilai = 90;
const result2 = `nama = ${nama} \nnilai = ${nilai} \nlulus = ${nilai > 80 ? 'ya' : 'tidak'}`; 
console.log(result2);
// result 2 ilmu baru bisa pake perbandingan di dalam string template, pake ternary operator


// bisa dipake buat multiline string, jadi ga perlu pake \n
const result3 = `nama 
saya
radithya`;
console.log(result3);