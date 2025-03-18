let day = parseInt(prompt("Введіть день тіжня (від 1 до 7):"));

switch (day) {
    case 1:
        alert("Понеділок");
        break;
    case 2:
        alert("Вівторок");
        break;
    case 3:
        alert("Середа");
        break;
    case 4:
        alert("Четверг");
        break;
    case 5:
        alert("П'ятниця");
        break;
    case 6:
        alert("Суббота");
        break;
    case 7:
        alert("Неділя");
        break;
    default:
        alert("Невірний номер тижня. Введіть число від 1 до 7.");
        break;
}