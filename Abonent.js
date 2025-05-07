class Abonent {
    constructor(name, number) {
      this.name = name;
      this.number = number;
    }
  
    getInfo() {
      return `Ім’я: ${this.name}, Номер: ${this.number}`;
    }
  }
  
  const phoneBook = [];
  
  document.getElementById("addBtn").addEventListener("click", function () {
    const name = document.getElementById("nameInput").value;
    const number = document.getElementById("numberInput").value;
  
    const newAbonent = new Abonent(name, number);
  
    phoneBook.push(newAbonent);
  
    updateDisplay();
  });
  
  function updateDisplay() {
    const listDiv = document.getElementById("abonentList");
    listDiv.innerHTML = "";
  
    phoneBook.forEach((abonent, index) => {
      const p = document.createElement("p");
      p.textContent = abonent.getInfo();
      listDiv.appendChild(p);
    });
  }