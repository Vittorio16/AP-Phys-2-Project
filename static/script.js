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
  let isImage = document.getElementById("graph");
  console.log(isImage.value);
  if (isImage.value == "True") {
    console.log("hiding");
    document.getElementById("input-form").style.display = "none";
    document.getElementById("info-paragraph").style.display = "none";

  }
  else {
    console.log("not hiding");
    document.getElementById("input-form").style.display = "inline-block";
    document.getElementById("info-paragraph").style.display = "block";

  }
}