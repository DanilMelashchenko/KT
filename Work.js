//***1***
let name = "Іван";
let city = name;
console.log(name);

let name2 = "Olga";
console.log(`привіт ${1}`);
console.log(`привіт ${"name2"}`);
console.log(`привіт ${name2}`);

let a = "5";
let b = "13cvb";
let c = "12.9sxdxfgv";
console.log(Number(a), typeof Number(a));
console.log(parseInt(b), typeof parseInt(b));
console.log(parseFloat(c), typeof parseFloat(c));

console.log ((0.1+0.2).toFixed(1));

console.log(Math.max(20, 10, 50, 40));

let randomNum = Math.floor(Math.random() * (4-2) +2)
console.log(randomNum);

const messege = "Welcome to Bahamas!";
console.log(messege.length);

console.log(messege.toUpperCase());

let persone = {};
persone.name = "Vanya";
persone.age = 25;
persone.city = "Kiyev";
console.log(persone);
delete persone.city;
persone["like flowers"] = true;
console.log(persone);

for (let key in persone) {
    console.log(`${key}: ${persone[key]}`);
}