
function copyToClipboard(id) {
  const copyText = document.getElementById(id);
  copyText.setSelectionRange(0, 99999); // For mobile devices
  navigator.clipboard.writeText(copyText.value);
}

function toggle(ids) {
  for (let i = 0; i < ids.length; i++) {
    const id = ids[i];
    const button = document.getElementById(`${id}-button`);
    const div = document.getElementById(id);
    button.classList.toggle("button-primary-filled");
    button.classList.toggle("button-primary-hollow");
    if (div.style.display == "block") {
      div.style.display = "none";
    } else {
      div.style.display = "block";
    }
  }
}
