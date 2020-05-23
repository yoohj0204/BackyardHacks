// functions for background music player
function playBgm() {
    const mp = document.getElementById("bgm");
    mp.play();
}
playBgm();

function pauseBtn() {
    const mp = document.getElementById("bgm");
    mp.pause();
}
// const buttons = document.querySelectorAll(".macabutton.w-inline-block");
// buttons.forEach(btn => {
//     btn.addEventListener("click", pauseBtn);
// });


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
