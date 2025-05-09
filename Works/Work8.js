let num1 = parseInt(prompt("Введіть перше число:"));
let num2 = parseInt(prompt("Введіть друге число:"));

let andResult = num1 & num2;
let orResult = num1 | num2;
let xorResult = num1 ^ num2;
let leftShiftResult = num1 << 1;
let rightShiftResult = num1 >>1;

alert(`Побітові операції:
    & = ${andResult}
    | = ${orResult}
    ^ = ${xorResult}
    << = ${leftShiftResult}
    >> = ${rightShiftResult}`);