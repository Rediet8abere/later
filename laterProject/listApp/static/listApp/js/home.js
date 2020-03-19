(function() {

    const slides = document.getElementById('slides')
    const slidesInner = slides.querySelector('.slides-inner')
    const images = slidesInner.querySelectorAll('img')
    const slideWidth = slides.clientWidth

    const nextButton = slides.querySelector('.play-next-button')
    const prevButton = slides.querySelector('.play-previous-button')

    let index = 0

    if (nextButton !== null) {
        nextButton.addEventListener('click', function(e) {
            e.preventDefault()

            nextSlide()
        })
    }

    if (prevButton !== null) {
        prevButton.addEventListener('click', function(e) {
            e.preventDefault()

            prevSlide()
        })
    }

    function nextSlide() {
        index +=1 
        if (index === images.length) {
            index = 0 
        }
        slidesInner.style.transform = `translate3d(${index * -slideWidth}px,0,0)`
    }

    function prevSlide() {
        if(index < 0) {
            index = images.length -1
        } else  {
            index -= 1
        }
        slidesInner.style.transform = `translate3d(${index * -slideWidth}px,0,0)`
    }

    setInterval(function() {
        nextSlide()
    }, 5000)
    

    }) ()