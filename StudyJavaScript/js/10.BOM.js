// Size, (prokrutka), coordinates

// BOM
const mainElement = document.documentElement; // html
// size, where we can work (html)
console.log(mainElement.clientWidth); // [output] 330
console.log(mainElement.clientHeight); // [output] 302

// size for browser with (prokrutka)
console.log(window.innerWidth); // [output] 330
console.log(window.innerHeight); // [output] 302

const h1 = document.querySelector('h1');

const new_p = document.createElement('p');
new_p.innerText = 'Test';
new_p.style.paddingTop = '1000px';
h1.insertAdjacentElement('afterend', new_p);

// calculate for all browser
const scrollWidth = Math.max(
    document.body.scrollWidth, document.documentElement.scrollWidth,
    document.body.offsetWidth, document.documentElement.offsetWidth,
    document.body.clientWidth, document.documentElement.clientWidth
);
const scrollHeight = Math.max(
    document.body.scrollHeight, document.documentElement.scrollHeight,
    document.body.offsetHeight, document.documentElement.offsetHeight,
    document.body.clientHeight, document.documentElement.clientHeight
);
console.log(scrollWidth); // [output] 313 (width with prokrutka)
console.log(scrollHeight); // [output] 1150 (height with prokrutka)

// how much px scrolling (from top) - only read
console.log(window.pageXOffset); // [output] 0
console.log(window.pageYOffset); // [output] 54.125

// scrollBy() - scroll from current state
// window.scrollBy(0, 100); // 0 - for x, 50 - for y

// scrollTo() - scroll for absolute coordinate (or scroll())
// window.scrollTo(0, 150);
// window.scrollTo({top: 400, left: 0, behavior: 'smooth'}); // smooth - small speed for scroll
// instant - big speed for scroll
// auto - default
// no work in Safari

// scrollIntoView(element) - scroll to element
// new_p.scrollIntoView(); // default: true (element in top for page), false (element in bottom for page)
new_p.scrollIntoView({
    // where show our element for y
    // start, center, end, nearest, default: center
    block: 'center',
    // where show our element for x
    // start, center, end, nearest, default: nearest
    inline: 'nearest',
    // speed for scroll 
    // auto, smooth, default: auto
    behavior: 'smooth',
});
// no work in Safari

// lock scroll
// document.body.style.overflow = 'hidden';

// -------------------------------------------------------------------

// Elements in page

// offsetParent - parent, where set position
// 1. parent-element, where use position: ...
// or
// 2. tags <td>, <th>, <table>
// or
// 3. tag <body>
// return null:
// 1. display: none or hidden
// 2. it's <body> or <html>
// 3. position: fixed
console.log(new_p.offsetParent); // [output] body-object

// how much move for parent
console.log(new_p.offsetLeft); // [output] 8
console.log(new_p.offsetTop); // [output] 80

// size for object (0 - if dispal: none)
console.log(new_p.offsetWidth); // [output] 297 
console.log(new_p.offsetHeight); // [output] 1018

// size for border (from inside to outside)
console.log(new_p.clientTop); // [output] 0
console.log(new_p.clientLeft); // [output] 0

// size without border or scroll
console.log(new_p.clientWidth); // [output] 297
console.log(new_p.clientHeight); // [output] 1018

// size with scroll
console.log(new_p.scrollWidth); // [output] 297
console.log(new_p.scrollHeight); // [output] 1018 

// how much scroll (we can set our and scroll)
console.log(new_p.scrollLeft); // [output] 0
console.log(new_p.scrollTop); // [output] 0
new_p.scrollTop = 150;

// scrollBy(), scrollTo(), scrollIntoView() work with object too

// -------------------------------------------------------------------

// Coordinate
// clientX, clientY - coordinate for browser (BOM)
// pageX, pageY - coordinate for page (DOM)

// for browser
console.log(new_p.getBoundingClientRect()); // [output] DOMRect {x: 8, y: 80.47.., ...}

// for page
console.log(new_p.getBoundingClientRect().top + window.pageYOffset); // [output] 80.47...

// elementFromPoint - get element for coordinate (for window)
console.log(document.elementFromPoint(8, 80.47)); // [output] <p style="padding-top: 1000px;">Test</p>



