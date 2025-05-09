function Colculator () {
    this.read = function () {
        this.a = +prompt ("Введіть перше число: ", "0");
        this.b = +prompt ("Введыть дрге число: ", "0");
    };

    this.sum = function () {
        return this.a + this.b;
    };

    this.mul = function () {
        return this.a * this.b;
    };
}

const calc = new Colculator ();

calc.read ();

console.log ("Сума: ", calc.sum());

console.log ("Добуток: ", calc.mul());