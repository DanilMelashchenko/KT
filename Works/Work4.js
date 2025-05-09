let userResponse = prompt("Чи маєте ви абонемент? (так/ні)").toLowerCase();
let hasSubscription = (userResponse === "так");

if(hasSubscription) {
    alert("Доступ дозволенно");
} else {
    let balance = parseFloat(prompt("Скільки грошей на рахунку?"));
    if (balance >=100) {
        alert("Доступ дозволенно")
    } else{
        alert("Доступ забороненно")
    }
}