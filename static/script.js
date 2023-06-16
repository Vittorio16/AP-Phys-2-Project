window.addEventListener("load", displayText);

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