   document.addEventListener("DOMContentLoaded", () => {
    });
function toggleCheckboxContainer() {
  const checkboxContainer = document.getElementById('checkbox-container');
  checkboxContainer.classList.toggle('active');
}


function domReady(fn) {
    if (
        document.readyState === "complete" ||
        document.readyState === "interactive"
    ) {
        setTimeout(fn, 1000);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}


function hideDiv(event) {
    const parentElement = event.target.parentElement;
    if (parentElement) {
        parentElement.style.display = 'none';
    }
}
function toggle_faq(id) {
    var el = document.getElementById(id);
    if (el.style.display == 'none') {
        el.style.display = 'block';
    } else {
        el.style.display = 'none';
    }

}
