const nilaiUjian = 80;
const nilaiAbsen = 90;

const lulusUjian = nilaiUjian > 80;
const lulusAbsen = nilaiAbsen > 85;

const lulus = lulusUjian && lulusAbsen;
console.log("apakah lulus? " + lulus);

const lulusSalahSatu = lulusUjian || lulusAbsen;
console.log("Apakah lulus salah satu " + lulusSalahSatu);s