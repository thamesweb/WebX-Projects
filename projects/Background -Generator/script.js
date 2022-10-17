var css = document.querySelector("p");
var color1 = document.querySelector(".color1");
var color2 = document.querySelector(".color2");
var body = document.getElementById("gradient");

function setgradient()
{
    body.style.background = "linear-gradient(to right, " + color1.value + ", " + color2.value + ")";
    document.getElementById("para").innerHTML = color1.value + " " + color2.value;
}