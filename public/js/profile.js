const submitButton = document.querySelector(".button-form");

submitButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = document.getElementById("name").value,
          dietres = document.getElementById("Dietary-Restrictions").value,
          allergy = document.getElementById("Allergies").value,
          healthconc = document.getElementById("Health-Concerns").value;
          
    if(username === "" || dietres === "" || allergy === "" || healthconc === "") {
        const warning = document.querySelector(".w-form-fail");
        warning.style.display = "block";
    } else {
        document.getElementById("email-form").submit();
    }
});
