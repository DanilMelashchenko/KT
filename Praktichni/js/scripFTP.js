const tree = document.getElementById("tree");

tree.addEventListener("click", function (event) {
    const li = event.target.closest("li");

    if (!li) return;

    const childUl = li.querySelector("ul");

    if (childUl) {
        childUl.hidden = !childUl.hidden;
    }
});
