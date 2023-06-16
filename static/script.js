window.addEventListener("load", displayText);

function displayText() {
  let isImage = document.getElementById("graph");
  if (isImage.value == "True") {
    document.getElementById("input-form").style.display = "none";
    document.getElementById("info-paragraph").style.display = "none";

  }
  else {
    document.getElementById("input-form").style.display = "inline-block";
    document.getElementById("info-paragraph").style.display = "block";
  }
}