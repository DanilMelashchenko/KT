const target = document.getElementById("target");
const hide = document.getElementById("hide");
const show = document.getElementById("show");

hide.addEventListener("click", () => {
    target.style.display = "none";
})

show.addEventListener("click" , () => {
    target.style.display = "block";
})