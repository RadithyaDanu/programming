// mirip while loop
// tapi disini pengecekan dilakukan setelah perulangan, jadi minimal 1x perulangan akan dilakukan meskipun
// kondisnya false
// sedangkan di while loop pengecekan dilakukan sebelum perulangan
// penggunaannya misal, mau nampilin menu, kita tampilin menu dulu baru nunggu use inpur pilihan, kalo dia pengen tutup
// yaudah tutup

let counter = 100
do {
    console.log(`ini adalah counter ke ${counter}`);
    counter++
} while(counter <= 10);

// jadi dieksekusi dulu baru dicek kondisinya, meskipun kondisinya diluar jangakuan pengecekan,
//  maka akan tetap tercetak
// kalo di while nggak
