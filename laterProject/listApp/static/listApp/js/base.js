<!-- Gallery JS -->
const galleryContainer = document.querySelector('.gallery-container');
const galleryControlsContainer = document.querySelector('.gallery-controls');
const galleryControls = ['previous', 'next'];
const galleryItems = document.querySelectorAll('.gallery-item');

class Carousel {
    constructor(container, items, controls) {
    this.carouselContainer = container;
    this.carouselControls = controls;
    this.carouselArray = [...items];
    }

    // Assign initial css classes for gallery and nav items
    setInitialState() {
    this.carouselArray[0].classList.add('gallery-item-first');
    this.carouselArray[1].classList.add('gallery-item-previous');
    this.carouselArray[2].classList.add('gallery-item-selected');
    this.carouselArray[3].classList.add('gallery-item-next');
    this.carouselArray[4].classList.add('gallery-item-last');

    document.querySelector('.gallery-nav').childNodes[0].className = 'gallery-nav-item gallery-item-first';
    document.querySelector('.gallery-nav').childNodes[1].className = 'gallery-nav-item gallery-item-previous';
    document.querySelector('.gallery-nav').childNodes[2].className = 'gallery-nav-item gallery-item-selected';
    document.querySelector('.gallery-nav').childNodes[3].className = 'gallery-nav-item gallery-item-next';
    document.querySelector('.gallery-nav').childNodes[4].className = 'gallery-nav-item gallery-item-last';
    }

    // Update the order state of the carousel with css classes
    setCurrentState(target, selected, previous, next, first, last) {

    selected.forEach(el => {
        el.classList.remove('gallery-item-selected');

        if (target.className == 'gallery-controls-previous') {
        el.classList.add('gallery-item-next');
        } else {
        el.classList.add('gallery-item-previous');
        }
    });

    previous.forEach(el => {
        el.classList.remove('gallery-item-previous');

        if (target.className == 'gallery-controls-previous') {
        el.classList.add('gallery-item-selected');
        } else {
        el.classList.add('gallery-item-first');
        }
    });

    next.forEach(el => {
        el.classList.remove('gallery-item-next');

        if (target.className == 'gallery-controls-previous') {
        el.classList.add('gallery-item-last');
        } else {
        el.classList.add('gallery-item-selected');
        }
    });

    first.forEach(el => {
        el.classList.remove('gallery-item-first');

        if (target.className == 'gallery-controls-previous') {
        el.classList.add('gallery-item-previous');
        } else {
        el.classList.add('gallery-item-last');
        }
    });

    last.forEach(el => {
        el.classList.remove('gallery-item-last');

        if (target.className == 'gallery-controls-previous') {
        el.classList.add('gallery-item-first');
        } else {
        el.classList.add('gallery-item-next');
        }
    });
    }

    // Construct the carousel navigation
    setNav() {
    galleryContainer.appendChild(document.createElement('ul')).className = 'gallery-nav';

    this.carouselArray.forEach(item => {
        const nav = galleryContainer.lastElementChild;
        nav.appendChild(document.createElement('li'));
    });
    }

    // Construct the carousel controls
    setControls() {
    this.carouselControls.forEach(control => {
        galleryControlsContainer.appendChild(document.createElement('button')).className = `gallery-controls-${control}`;
    });

    !!galleryControlsContainer.childNodes[0] ? galleryControlsContainer.childNodes[0].innerHTML = this.carouselControls[0] : null;
    !!galleryControlsContainer.childNodes[1] ? galleryControlsContainer.childNodes[1].innerHTML = this.carouselControls[1] : null;
    }

    // Add a click event listener to trigger setCurrentState method to rearrange carousel
    useControls() {
    const triggers = [...galleryControlsContainer.childNodes];

    triggers.forEach(control => {
        control.addEventListener('click', () => {
        const target = control;
        const selectedItem = document.querySelectorAll('.gallery-item-selected');
        const previousSelectedItem = document.querySelectorAll('.gallery-item-previous');
        const nextSelectedItem = document.querySelectorAll('.gallery-item-next');
        const firstCarouselItem = document.querySelectorAll('.gallery-item-first');
        const lastCarouselItem = document.querySelectorAll('.gallery-item-last');

        this.setCurrentState(target, selectedItem, previousSelectedItem, nextSelectedItem, firstCarouselItem, lastCarouselItem);
        });
    });
    }
}

const exampleCarousel = new Carousel(galleryContainer, galleryItems, galleryControls);

exampleCarousel.setControls();
exampleCarousel.setNav();
exampleCarousel.setInitialState();
exampleCarousel.useControls();

<!-- JS Background -->
const colors = ["#3CC157", "#2AA7FF", "#1B1B1B", "#FCBC0F", "#F85F36"];

const numBalls = 50;
const balls = [];

for (let i = 0; i < numBalls; i++) {
let ball = document.createElement("div");
ball.classList.add("ball");
ball.style.background = colors[Math.floor(Math.random() * colors.length)];
ball.style.left = `${Math.floor(Math.random() * 100)}vw`;
ball.style.top = `${Math.floor(Math.random() * 100)}vh`;
ball.style.transform = `scale(${Math.random()})`;
ball.style.width = `${Math.random()}em`;
ball.style.height = ball.style.width;

balls.push(ball);
document.body.append(ball);
}

balls.forEach((el, i, ra) => {
let to = {
    x: Math.random() * (i % 2 === 0 ? -11 : 11),
    y: Math.random() * 12
};

let anim = el.animate(
    [
    { transform: "translate(0, 0)" },
    { transform: `translate(${to.x}rem, ${to.y}rem)` }
    ],
    {
    duration: (Math.random() + 1) * 2000,
    direction: "alternate",
    fill: "both",
    iterations: Infinity,
    easing: "ease-in-out"
    }
);
});

<!-- Add A Book JS -->
anime.timeline({loop: true})
.add({
    targets: '.ml8 .circle-white',
    scale: [0, 3],
    opacity: [1, 0],
    easing: "easeInOutExpo",
    rotateZ: 360,
    duration: 1100
}).add({
    targets: '.ml8 .circle-container',
    scale: [0, 1],
    duration: 1100,
    easing: "easeInOutExpo",
    offset: '-=1000'
}).add({
    targets: '.ml8 .circle-dark',
    scale: [0, 1],
    duration: 1100,
    easing: "easeOutExpo",
    offset: '-=600'
}).add({
    targets: '.ml8 .letters-left',
    scale: [0, 1],
    duration: 1200,
    offset: '-=550'
}).add({
    targets: '.ml8 .bang',
    scale: [0, 1],
    rotateZ: [45, 15],
    duration: 1200,
    offset: '-=1000'
}).add({
    targets: '.ml8',
    opacity: 0,
    duration: 1000,
    easing: "easeOutExpo",
    delay: 1400
});

anime({
targets: '.ml8 .circle-dark-dashed',
rotateZ: 360,
duration: 8000,
easing: "linear",
loop: true
});
