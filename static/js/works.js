let box = document.getElementsByClassName('box');
for (let i = 0; i < box.length; i++) {
    box[i].addEventListener('mouseover', () => {
        box[i].classList.add('shadow');
    },false);
    box[i].addEventListener('mouseout', () => {
        box[i].classList.remove('shadow');
    },false);
}