window.addEventListener("load", setTimeout);
window.addEventListener("load", displayText);
// Hide error messages after a while
setTimeout(() => {
  const box = document.getElementById('error-message');

  box.style.display = 'none';

  // 👇️ hides element (still takes up space on page)
  // box.style.visibility = 'hidden';
}, 6000); // 👈️ time in milliseconds

function displayText() {
  isImage = document.getElementById("graph");
  if (isImage == "True") {
    document.getElementById("input-form").style.display = "none"
  }
  else {
    document.getElementById("input-form").style.display = "inline-block"
  }
}