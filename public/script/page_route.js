// routing function
//
function loadPage(route) {
    console.log("Loading page: " + route);
    fetch(route)
        .then((response) => response.text())
        .then((html) => {
            document.getElementById("main-page").innerHTML = html
        }).then(() => {

        });
    const navLinks = document.querySelector('.nav-links');
      if (navLinks && navLinks.classList.contains('active')) {
    navLinks.classList.remove('active'); // Remove the "active" class to hide it
    }
}


function loadScriptDynamically(src) {
  console.log("Loading script: " + src);
  const script = document.createElement('script');
  script.src = src; // URL of the JavaScript file
  script.type = 'text/javascript';
  script.async = true; // Optional: to load the script asynchronously
  document.head.appendChild(script); // Append to <head> or <body>
}
document.getElementById("toggle").addEventListener("click", function() {
  var list = document.getElementById("myList");
  if (list.classList.contains("expanded")) {
    list.classList.remove("expanded");
    list.style.maxHeight = "0";
    list.style.overflow = "hidden";
  } else {
    list.classList.add("expanded");
    list.style.maxHeight = "200px";
    list.style.overflow = "visible";
  }
});
