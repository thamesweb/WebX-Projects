
window.onscroll = function() { scrollFunction() };

function scrollFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.getElementById("nav").classList.add("round");
  } else {
		document.getElementById("nav").classList.remove("round");
  }
}


function nav() {
	document.getElementById("nav").classList.toggle("full");
	document.getElementById("hamburger").classList.toggle("close");
	document.getElementById("body").classList.toggle("no-overflow");
}

function intro() {
	var argumentOne = "New skills";
	
}

// -------------