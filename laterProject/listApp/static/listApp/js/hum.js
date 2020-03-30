let menuBtn = document.querySelector('.menu-btn')
let menu = document.querySelector('.menu')
// we want the menu to be closed when the webpage is open
let menuStatus = false;

// closes menu when the webpage is open
menu.style.marginLeft = '-300px';

function menuToggle() {
  if (menuStatus == false) {
    menu.style.marginLeft = '0px';
    menuStatus = true;
  }
  else if(menuStatus == true) {
    menu.style.marginLeft = '-300px';
    menuStatus = false;
  }
}

menuBtn.onclick = menuToggle;

//

let btn = document.querySelector('.test-link');
let form = document.querySelector('.test-form');

// take the defulat event which in this case is going back up
// to the top and change it to show the text 'YAY!'
// function firstFunction(e) {
//   e.preventDefault();
//   btn.innerHTML = 'YAY!';
// }
//
// function secondFunction() {
//   btn.style.backgroundColor = 'red';
// }

// event listener not working
// btn.addEventListener('click', firstFunction);
// btn.addEventListener('click', secondFunction);

// take the default event which in this case is going to script.php page
// and prevent it from happening
// function stopFormSubmit(e) {
//   e.preventDefault();
// }
//
// form.onclick = stopFormSubmit;
