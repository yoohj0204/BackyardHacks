// functions for prompting file selector
const cameraButton = document.querySelector(".macabutton-camera");
cameraButton.addEventListener("click", (e) => {
    $("#file-upload").trigger("click");
});

function triggerSubmit(e) {
    // $("#file-submit").trigger("click");
    // e.preventDefault();
    const uploadFile = document.getElementById("file-upload");
    // console.log(uploadFile.value);
    $("#file-submit").trigger("click");
}
