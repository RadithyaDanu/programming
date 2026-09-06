//mengubah nilai null atau undefined menjadi nilai default yang kita tentukan

let parameter;
let data = parameter;

if (data === null || data === undefined) {
    console.log("halo");
}

// jika nilainya bukan null atau undefined, maka outputnya akan sesuai dengan nilai tersebut

// ternary operator versi nullish coalesing

let ternary;
let result = ternary ?? "nilai default";
console.log(result);