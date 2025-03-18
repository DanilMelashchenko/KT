let balance = parseFloat(prompt("Введіть ваш баланс"));

balance += 500;
balance -= 200;
balance += balance * 0.05;

alert("Підсумковий баланс: " + balance + "грн");