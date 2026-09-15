let isOpen = false;
let jobPanel = document.getElementById("job-panel");
let catPanel = document.getElementById("cat-panel");
let tourPanel = document.getElementById("tour-panel");


function showPanel(which) {

    if (which == "job" && !isOpen) {
        jobPanel.style.display = "block";
        isOpen = true;
        jobPanel.classList.add("active");
    }

    if (which == 'cat' && !isOpen) {
        catPanel.style.display = "block";
        isOpen = true;
    }

    if (which === "tour" && !isOpen) {
        tourPanel.style.display = "block";
        isOpen = true;
    }

}

let closeButtons = document.getElementsByClassName('close-button');

for (let btn of closeButtons) {
    btn.addEventListener("click", function() {
        isOpen = false;
        jobPanel.classList.remove("active");
        jobPanel.style.display = 'none';
        catPanel.style.display = 'none';
        tourPanel.style.display = 'none';
    });
}