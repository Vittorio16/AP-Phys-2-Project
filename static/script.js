window.addEventListener("load", setTimeout);

// Hide error messages after a while
setTimeout(() => {
  const box = document.getElementById('error-message');

  box.style.display = 'none';

  // 👇️ hides element (still takes up space on page)
  // box.style.visibility = 'hidden';
}, 6000); // 👈️ time in milliseconds