//function tidak mengembalikan value
// untuk mengembalikan value, harus pake return
// return lalu diikuti dengan nilai yang ingin dikembalikan
// function hanya bisa mengembalikan satu value, kalo lebih pake array sebagai returnnya

// buat function dengan parameter dan return
function sayHello(firstName, lastName){
    const say = `halo ${firstName} ${lastName}, Selamat datang!`;
    return say;
}

// memanggil function dan menangkap hasil return valuenya
const result = sayHello("radithya", "danutirta");
console.log(result)
// jadi dengan menggunakan return, result bisa menyimpan hasil dari paramter sayHello
// jika gapake return, bakal mengembalikan undefined karena tidak mengembalikan value

sayHello("radit", "danu")
// disini kita memanggil function yang mengembalikan value tapi ga ditangkap, menyebabkan tidak menampilkan apa apa
// kita harus tangkep valuenya dengan const result = sayHello("radithya", "danutirta");
// jadi return value akan masuk ke dalam result



// function return value yang lebih dari satu
// misal ada kondisi dimana kita perlu return yang berbeda beda, ini bisa, misal
function getFinalScore(value){
    if (value > 90 ) {
        return "A";
        // mmisal disini dikasih return kedua (return "B"), ini gaakan dieksekusi karena return A sudah memenuhi 
        // jadi akan diabaikan
    } else if (value > 80) {
        return "B";
    } else if (value > 70) {
        return "C";
    } else {
        return "D";
    }
}

const final = getFinalScore(90);
console.log(final);


// jika kita menggunakan return, kode dibawahnya tidak akan dieksekusi lagi jika return sudah terpenuhi
//contoh

function isContains(array, searchValue){
    for (const items of array){
        console.log(`iterasi item ${items}`)
        if (items === searchValue){
            return true; // kalo items sama kayak apa yg dicari, maka langsung dihentikan dan return true
        }
    }
    return false; // setelah iterasi kalo ga nemu dia akan return false disini tanpa masuk ke return true
}

const data = [1,2,3,4,5,6,7,8,9];
const search = 3;
const found = isContains(data, search);
console.log(found)
