const bodyE1 = document.body;
const barE1 = document.querySelector('.bar');

const updateBar = () => {
    let scrollPos = (window.scrollY / (bodyE1.scrollHeight - window.innerHeight)) * 100;
    barE1.style.width = `${scrollPos}%`;
    requestAnimationFrame(updateBar);
};

updateBar();
