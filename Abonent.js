class Abonent {
    constructor(name, number){
        this.name = name;
        this.number = number;
    }

    setNumber (newNumber) {
        this.number = newNumber;
    }

    getInfo() {
        console.log(`Ім'я: ${this.name}, Номер: ${this.number}`);
    }
}

const user1 = new Abonent ("Олена", "123-456-88");
const user2 = new Abonent ("Іван", "987-654-22");
const user3 = new Abonent ("Марія", "555-878-77");

user1.getInfo();
user2.getInfo();
user3.getInfo();

user1.setNumber ("888-555-33");

user1.getInfo ();