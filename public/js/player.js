function playBgm() {
    const mp = document.getElementById("bgm");
    mp.play();
}
playBgm();

function pauseBtn() {
    const mp = document.getElementById("bgm");
    mp.pause();
}
const buttons = document.querySelectorAll(".macabutton.w-inline-block");
buttons.forEach(btn => {
    btn.addEventListener("click", pauseBtn);
});
