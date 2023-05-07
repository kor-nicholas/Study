// Events

// Attribute in html (onclick="js-code")

// or

const button = document.querySelector('button');

// rewrite function for onclick
button.onclick = function() {
    console.log('Click'); // [output] Click
}

// or

function showClickInConsole() {
    console.log('click');
}

// rewrite function for onclick
button.onclick = showClickInConsole;

// addEventListener(event, function, options) - no rewrite, just add listener
button.addEventListener('click', function() {
    console.log('Click');
});

button.addEventListener('click', showClickInConsole);

// after click [output] click; Click; click (all functions for 'onclick')

button.addEventListener('click', showClickInConsole, {
    // phase, when function must be run
    capture: false,
    // remove handler after run (work only once) 
    once: true,
    // anytime run preventDefault
    passive: false,
});

// removeEventListener(event, function, options) - delete listener for event
button.removeEventListener('click', showClickInConsole);

// after click [output] click, Click

// event - object in argument in handler with more details/options/info
// event.type - type of event ('click', ...)
// event.target - object, where event runs
// event.currentTarget - object, where we add listener
// event.clientX and event.clientY - coordinates mouse-coursor

function showConsole(event) {
    console.log(event.type); // [output] click
    console.log(event.target); // [output] <button>Click</button>
    console.log(event.currentTarget); // [output] <button>Click</button>
    console.log(`${event.clientX}:${event.clientY}`); // [output] 21:84
    console.log(event); // [output] PointerEvent {isTrusted: true, ...}
};

button.addEventListener('click', showConsole);

let buttons = document.querySelectorAll('button');

// Vsplitie (run handler for all parents to top)
// block1
//  block2
//   block3
// click for block3 -> run handler for block3, block2, block1
// event.stopPropagation() - stop vsplitie, run handler only for this block

// Pogruzhenie 
// block1
//  block2
//   block3
// set capture: true in options in block2
// click for block3 -> run handler for block2, block3, block1

// Delegate event
// create 1 listener for parent, because listeners load browser
const body = document.body;

body.addEventListener('click', function(event) {
    // if element where run event is button
    if(event.target.closest('button')) {
        showClickInConsole();
    }
});

// Default event in browser
// options passive: true - no turn off defautl event 
// event.preventDefault() -> error
const link = document.querySelector('a');

link.addEventListener('click', function(event) {
    console.log('Our code');
    // turn off default event for browser
    // for link or tag a -> no go to page
    event.preventDefault();
});

// or

// link.onclick = function() {
//     console.log('Our code...');
//     return false;
// }

// Event

// mouse: 
// mousedown/mouseup - mouse down or up for element
// mouseover/mouseout - cursor (poyavlyaetsa) or (yxodit) for element
// mouseenter/mouseleave - like mouseover/mouseout, but without vsplitie
// mousemove - every (dvizenie) on element
// contextmenu - right click

// complex
// click = mousedown + mouseup
// dblclick - click twice for element

// event.which -> 1 or 2 or 3 (left click, center or koleso, right click)

buttons[1].addEventListener('mousedown', function(event) {
    console.log(`Click for ${event.which} button`); // [output] Click for 1 button; Click for 3 button
});
buttons[1].addEventListener('click', function(event) {
    console.log('Mouse up and as a rusult -> click');
});
buttons[1].addEventListener('contextmenu', function(event) {
    console.log('Context menu');
});
buttons[1].addEventListener('mousemove', function(event) {
    buttons[1].insertAdjacentHTML('afterend', `<p>X: ${event.clientX} | Y: ${event.clientY}</p>`);
});
buttons[2].addEventListener('mouseover', function(event) {
    console.log('Cursor over on element');
    // target - cursor to over(goal, our element) 
    console.log(event.target); // [output] <button>Click</button>
    // relatedTarget - cursor from over(start over for our element)
    console.log(event.relatedTarget); // [output] html (body)
});
buttons[2].addEventListener('mouseout', function(event) {
    console.log('Cursor out on element');
    // target - cursor from over(start over for our element)
    console.log(event.target); // [output] <button>Click</button>
    // relatedTareget - cursor to over(goal, our element) 
    console.log(event.relatedTarget); // [output] html (body)
});
// if over for children-element -> vsplitie(mouseover, mouseout, mouseover)
// with mousecenter/mouseleave -> no vsplitie

// keyboard:
// keydown/keyup - key down or up
// event.code - code for key
// event.key - value of key
document.addEventListener('keydown', function(event) {
    console.log(`Down for ${event.code} (${event.key}) key`);
});
document.addEventListener('keyup', function(event) {
    console.log(`Up for ${event.code} (${event.key}) key`);
});
// check Ctrl + Z (no think about language, if user change it)
document.addEventListener('keydown', function(event) {
    if(event.code == 'KeyZ' && (event.ctrlKey || event.metaKey)) {
        console.log('Cancel (becaue user use CtRL + Z)');
    }
});
// repeat - if we key down and no up, return true
document.addEventListener('keydown', function(event) {
    console.log(event.repeat);
});

// example in textarea
const txtItem = document.querySelector('.textarea__item');
const txtItemList = txtItem.getAttribute('maxlength');
const txtCounter = document.querySelector('.textarea__counter span');
txtCounter.innerHTML = txtItemList;

txtItem.addEventListener('keyup', txtSetCounter);
txtItem.addEventListener('keydown', function(event) {
    if(event.repeat) txtSetCounter();
});

function txtSetCounter() {
    const txtCounterResult = txtItemList - txtItem.value.length;
    txtCounter.innerHTML = txtCounterResult;
};

// scrolling:
// scroll - event when scroll
// event.preventDefault() - no work
window.addEventListener('scroll', function(event) {
    // how much px scrolled
    console.log(this.scrollX);
    console.log(this.scrollY);
});

// download page:
// DOMContentLoaded - load all html (css and img, ... - no must)
// load - load all html (+ css and img, ...)
// beforeunload/unload - user close page

// document.readyState - state for loading
// 'loading' - page loading
// 'interactive' - page all readed (only html)
// 'complete' - page all readed (html + css, img, ...)

document.addEventListener('DOMContentLoaded', readyDom);

window.addEventListener('load', readyLoad);

function readyDom() {
    const image = document.querySelector('img');
    console.log(document.readyState); // [output] interactive
    console.log('DOM loaded');
    console.log(image.offsetWidth); // [output] 1920 (in theory must be 0)
};

function readyLoad() {
    console.log(document.readyState); // [output] complete
    const image = document.querySelector('img');
    console.log('Page loaded');
    console.log(image.offsetWidth); // [output] 1920
};

// if user a lot of write data in form and click for reload - ask user
window.addEventListener('beforeunload', function(event) {
    event.preventDefault(); // must be for standart
    event.returnValue = ''; // need for Chrome
});
// when user close, but we can work in (phon)
window.addEventListener('unload', function(event) {
    // https://w3c.github.io/beacon
});



