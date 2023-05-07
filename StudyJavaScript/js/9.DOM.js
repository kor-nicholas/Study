// Browser (Okruzenie)
// window:
// DOM (document) - Document Object Model
// BOM (navigator, location, history) - Browser Object Model
// JavaScript (Object, Array, Function)
// CSSOM (work with CSS in page) - CSS Object Model

// DOM (html/css)

// tags in html - object in DOM
// document - start in DOM
// (include js-script in end of html to js can load all objects)

const htmlElement = document.documentElement;
const headElement = document.head;
const bodyElement = document.body;

console.log(htmlElement); // [output] html-object
console.log(headElement); // [output] head-object
console.log(bodyElement); // [output] body-object

// -------------------------------------------------------------------

// Navigation for DOM
// NodeList - html with (yzli), HTMLCollection - only html

// NodeList
console.log(htmlElement.firstChild); // [output] head-object
console.log(htmlElement.lastChild); // [output] body-object
console.log(headElement.firstChild); // [output] #text
console.log(headElement.lastChild); // [output] #text
console.log(bodyElement.firstChild); // [output] #text
console.log(bodyElement.lastChild); // [output] script-object

console.log(bodyElement.childNodes); // [output] NodeList(8) [text, h1, text, h3, text, div.lesson, text, script]
console.log(bodyElement.hasChildNodes()); // [output] true

console.log(bodyElement.previousSibling); // [output] #text
console.log(bodyElement.nextSibling); // [output] null
console.log(bodyElement.parentNode); // [output] html-object

// HTMLCollection
console.log(bodyElement.children); // [output] HTMLCollection(4) [h1, h3, div.lesson, script]

// for (const node of bodyElement.childNodes) {
//     console.log(node);
// }

console.log(bodyElement.firstElementChild); // [output] h1
console.log(bodyElement.lastElementChild); // [output] script
console.log(bodyElement.parentElement); // [output] html-object

console.log(bodyElement.previousElementSibling); // [output] head
console.log(bodyElement.nextElementSibling); // [output] null

// -------------------------------------------------------------------

// Search

// querySelector() (search for css-selector) - return first element, that find
// querySelectorAll() - return collection with data (if one - collection with 1 element)
// Return static collection (data only from html)
console.log(document.querySelector('.yellow')); // [output] span.yellow
console.log(bodyElement.querySelector('h1')); // [output] h1
// document.querySelector('.lesson__list, .lesson__text'); // find classes lesson__list and lesson__text
// document.querySelector('.lesson__list .lesson__text'); // find class lesson__text in class lesson__list
// document.querySelector('#listItem'); // find by id
// document.querySelector('[onclick="sendData()"]'); // find by attribute

let yellow = document.querySelector('.yellow');

// getElementById('id') - only in document
// getElementsByTagName('tagName')
// getElementsByClassName('className')
// getElementsByName('name') - only in document, find for value in attribute
// Return live collection (data from html and js too)

// closest('selector') - find parent near top ('selector' - element that we search) 
console.log(yellow.closest('.yellow')); // [output] span.yellow; h1; span.yellow

// matches('selector') - check selector for element
console.log(yellow.matches('.yellow')); // [output] true
console.log(yellow.matches('body')); // [output] false

// -------------------------------------------------------------------

// Add our HTML from JS

// innerHTML - get value from html-object
console.log(yellow.innerHTML); // [output] JavaScript
yellow.innerHTML = '<span style="color: yellow;">New Text</span>'; // change html

// outerHTML - get all html-object
console.log(yellow.outerHTML); // [output] <span class="yellow"><span style="color: yellow;">New Text</span></span>
yellow.outerHTML = '<span style="color: yellow">JavaScript</span>';
// but, we return old html
console.log(yellow.outerHTML); // [output] <span class="yellow"><span style="color: yellow;">New Text</span></span>

// textContent - work with only text (get data from form to user can't add html-code and change our html)
console.log(yellow.textContent); // [output] New Text (but in page other text)
yellow.textContent = 'Random';
console.log(yellow.textContent); // [output] Random (but in page other text)

// data (from comment)
// <!-- It's comment --> - object
// object.data -> It's comment
// object.data = 'new comment'; -> set new comment

let lesson__text = document.querySelector('.lesson__text');

// createElement('tagName');
const newElement = document.createElement('div');
console.log(newElement); // [output] <div></div>
newElement.innerHTML = '<p>It\'s new paragraph</p>';
// lesson__text.before(newElement); // add before our element
// lesson__text.after(newElement); // add after our element
// lesson__text.prepend(newElement); // add inside our element and start old value
lesson__text.append(newElement); // add inside our element and end old value
lesson__text.append('new text'); // add new only text in value for element

/*
<!-- before -->
<ul class="lesson__list">
    <!-- prepend -->
    <li>Number 1</li>
    <li>Number 2</li>
    <li>Number 3</li>
    <!-- append -->
</ul>
<!-- after --> 
*/

// insertAdjacentHTML('beforebegin/afterbegin/beforeend/afterend', 'html')
// beforebegin - add html before element
// afterbegin - add html inside element and start old value
// beforeend - add html inside element and end old value
// afterend - add html after element
lesson__text.insertAdjacentHTML('afterbegin', '<img src="../../img/index.jpeg">');

/*
<!-- beforebegin -->
<ul class="lesson__list">
    <!-- afterbegin -->
    <li>Number 1</li>
    <li>Number 2</li>
    <li>Number 3</li>
    <!-- beforeend -->
</ul>
<!-- afterend --> 
*/

// insertAdjacentText('beforebegin/afterbegin/beforeend/afterend', 'text')
// add only text (if text has html -> no use it)
// insertAdjacentElement('beforebegin/afterbegin/beforeend/afterend', 'element')
// add new element, that created with help document.createElement('div')

// Move element (append())
lesson__text.append(yellow); // move text Random

// Copy element (cloneNode(true))
// true - copy value in element too, without true - copy only element
let clone = yellow.cloneNode(true); // copy Random text
lesson__text.append(clone);

// Delete element
clone.remove(); // delete copy Random text

// -------------------------------------------------------------------

// Work with CSS and classes

// className - get all classes for element
console.log(lesson__text.className); // [output] lesson__text
// change for new class (rewrite all old classes)
lesson__text.className = 'lesson__text';

// classList - add/delete 1 class
lesson__text.classList.add('active'); // lesson__text active
lesson__text.classList.remove('active'); // lesson__text
lesson__text.classList.toggle('active'); // if hasn't class -> add new class, if has class -> delete this class
lesson__text.classList.contains('active'); // chechk, has element class or no? true/false

// for(let className of lesson__text.classList) {
//     console.log(className);
// }

// CSS
yellow.style.color = 'red';
// lowerCamelCase - if style has 2 or more words
yellow.style.marginBottom = '10px';
yellow.style.zIndex = '10';
console.log(yellow.style.color); // [output] red (only from attribute style in html)
yellow.style.marginBottom = ''; // delete css style
yellow.style.cssText = `
    font-size: 20px;
    color: green;
    text-align: center;
`; // add more styles (rewrite all old styles)

// only read styles
console.log(getComputedStyle(yellow).marginBottom); // [output] 0px
console.log(getComputedStyle(yellow, '::before').backgroundColor); // [output] rgba(0, 0, 0, 0) (get styles for psevdo-element)

// Attributes
// <a href="https://google.com">Google</a>
// let link = document.querySelector('a');
// console.log(link.href); // [output] https://google.com
console.dir(lesson__text); // [output] div.lesson__text.active (all attributes for element)

console.log(lesson__text.hasAttribute('name')); // [output] false
console.log(lesson__text.getAttribute('class')); // [output] lesson__text active
console.log(lesson__text.setAttribute('name', 'value')); // [output] undefined
console.log(lesson__text.hasAttribute('name')); // [output] true
console.log(lesson__text.removeAttribute('name')); // [output] undefined

// all atributes that start for 'data' -> must use field dataset
lesson__text.dataset.size = '5810'; // set data-size
console.log(lesson__text.dataset.size); // [output] 5810
// data-size-value -> dataset.sizeValue

console.log(yellow.tagName); // [output] SPAN
// yellow.hidden = true; // hidden element (Random text)



