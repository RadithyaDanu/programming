const nilai = "A"

switch (nilai) {
    case "A" : 
        console.log("lulus");
        break;
    case "B" :
    case "C" :
        console.log("nilai ok");
        break
    case "D" :
        console.log("lulus bersyarat");
        break;
    default :
        console.log("salah jurusan");
        break;
}

// switch ini mirip if statement, namun lebih simpel
// switch hanya digunakan untuk penggunaan perbandingan ==
// case itu if dan else if
// default itu else
// penggunaan break disini bertujuan agar jika kondisi terpenuhi, program akan berhenti