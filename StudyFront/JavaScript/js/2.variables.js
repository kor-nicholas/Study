// let - create variable 
let age;
let info123;
let $size;
let _color;

// lowerCamelCase
let leftSidebarSize;

let myLifeStyle = 'freelance', myAge = 20;
let myLifeStyle2 = 'freelance', 
    myAge2 = 20;

myLifeStyle = myAge; // no error for string and int

// -------------------------------------------------------------------

// const - can't change
// if we know value
const BLOCK_SIZE = 25
const COLOR_RED = "#F00";
// if we dont't know value
const summSizes = 25 + 30;

// -------------------------------------------------------------------

// var - create variable (before let/const)
// if use conditional (if/while/for/...)
if(true) {
    let test = 'test';
}
console.log(test); // no find

if(true) {
    var test = 'test';
}
console.log(test); // [output] test

// -------------------------------------------------------------------

// Types of data (dynamic tipization)
console.log(typeof test); // [output] string

// Undefined (if create var, but not =)
let userName;
console.log(typeof userName); // [output] undefined
console.log(userName); // [output] undefined

if (userName === undefined || typeof userName === undefined) {
    console.log('Var isn\'t ='); // [output] Var isn't =
}

// -------------------------------------------------------------------

// Null (nothing)
let block = document.querySelector('.block');
console.log(block); // [output] null
console.log(typeof block); // [output] object (error from js)

// -------------------------------------------------------------------

// Boolean (true/false)
let trueOrFalse = 58 < 18;
console.log(trueOrFalse); // [output] false

let userAge = 58;
console.log(typeof userAge); // [output] number
userAge = Boolean(userAge);
console.log(userAge); // [output] true
console.log(typeof userAge); // [output] boolean

userAge = 0;
console.log(typeof userAge); // [output] number
userAge = Boolean(userAge);
console.log(userAge); // [output] false
console.log(typeof userAge); // [output] boolean

userAge = ' ';
console.log(typeof userAge); // [output] number
userAge = Boolean(userAge);
console.log(userAge); // [output] true
console.log(typeof userAge); // [output] boolean

userAge = '';
console.log(typeof userAge); // [output] number
userAge = Boolean(userAge);
console.log(userAge); // [output] false
console.log(typeof userAge); // [output] boolean

// -------------------------------------------------------------------

// Number
userAge = 18;
let userHight = 1.83;
console.log(userAge); // [output] 18
console.log(typeof userAge); // [output] number
console.log(userHight); // [output] 1.83
console.log(typeof userHight); // [output] number
// Infinity (beckonechnost, more then some number)
let getInfinity  = 58 / 0;
console.log(getInfinity); // [output] Infinity
console.log(typeof getInfinity); // [output] number
// NaN (error in math)
let getNan = 'Freelancer' / 10;
console.log(getNan); // [output] NaN
console.log(typeof getNan); // [output] number

userAge = '24';
console.log(typeof userAge); // [output] string
userAge = Number(userAge);
console.log(typeof userAge); // [output] number

userAge = '72' / '2';
console.log(userAge); // [output]
console.log(typeof userAge); // [output] number

let num = 255;
console.log(num.toString(16)); // [output] ff (255 in 16-s system)
console.log(num.toString(8)); // [output] 377 (255 in 8-s system)
console.log(num.toString(2)); // [output] 11111111 (255 in 2-s system)

// Round
// FLoor (round in less)
let numOne = Math.floor(5.8); // 5
let numTwo = Math.floor(-2.2); // -3
// Ceil (round in more)
let numOne2 = Math.ceil(5.8); // 6
let numTwo2 = Math.ceil(-2.2); // -2
// Round (to near int)
let numOne3 = Math.round(5.5); // 6 (5.4 -> 5)
let numTwo3 = Math.round(-2.2); // -2
// toFixed (after ',' and return string)
let numOne4 = +5.845.toFixed(2); // 5.84 (+ to convert in number)

console.log(isNaN(25 + 'Hello')); // [output] True
// because (NaN === NaN -> false)
if(25 + 'Hello' !== NaN) {
    console.log('I\'m not NaN'); // [output] I'm not NaN
}

console.log(+'150px'); // [output] NaN
// so
console.log(parseInt('150px')); // [output] 150
console.log(parseFloat('150.58px')); // [output] 150.58

console.log(Math.random()); // [output] ... (random number >= 0 and < 1)
console.log(Math.max(1, 5, 9)); // [output] 9
console.log(Math.min(1, 5, 9)); // [output] 1
console.log(Math.abs(-58)); // [output] 58 (module)
console.log(Math.pow(2, 4)); // [output] 16 (2 ^ 4 or 2 ** 4)

// -------------------------------------------------------------------

// BigInt
// values for number 9007199254740991 -9007199254740991
const bigInt = 12345678901234567890n;
console.log(typeof bigInt);

let someBigNum = 1e6; // 1 * 10 ^ 6 = 1000000
let someLittleNum = 1e-6; // 1 * 10 ^ -6 = 0.000001

// -------------------------------------------------------------------

// String
// "" or '' - doesn't matter, but `` - add var
let userSlog = "Relax, but work in free time";
let userSlog2 = 'Relax, but work in free time';
let userSlog3 = `Relax, but work in free time (slogan for ${age})`;
let userSlog4 = `Hello
I'm freelancer`;

userAge = 30;
console.log(typeof userAge); // [output] number
userAge = String(userAge);
console.log(typeof userAge); // [output] string

trueOrFalse = true;
console.log(typeof trueOrFalse); // [output] boolean
trueOrFalse = String(trueOrFalse);
console.log(trueOrFalse); // [output] true
console.log(typeof trueOrFalse); // [output] string

// use symbols UTF-16 and UTF-32
console.log('\u00A9 \u{1f60D}'); // [output] © 😍

console.log(userSlog.length); // [output] 28
console.log(userSlog[0]); // [output] R
console.log(userSlog[userSlog.length - 1]); // [output] e (last char)

for(const char of userSlog) {
    console.log(char); // [output] R, e, l, a, x, ' ', ...
}

userSlog[0] = '.';
console.log(userSlog[0]); // [output] R (we can't change symbol in text)

console.log(userSlog.toUpperCase()); // [output] RELAX, BUT WORK IN FREE TIME
console.log(userSlog.toLowerCase()); // [output] relax, but work in free time

console.log(userSlog.indexOf('but')); // [output] 7 (find index for sub-text)
console.log(userSlog.indexOf('but', 2)); // [output] 7 (find index for sub-text from index = 2)
console.log(userSlog.indexOf('jbhnkgjksdn')); // [output] -1 (because it doesn't find sub-text)

// like indexOf
console.log(userSlog.includes('but')); // [output] true
console.log(userSlog.includes('hbjfkjsdf')); // [output] false
console.log(userSlog.startsWith('kjfs')); // [output] false (bacause start isn't sub-text)
console.log(userSlog.endsWith('time')); // [output] true (because last sub-text is 'time')

// 1 - include, 6 - not include
console.log(userSlog.slice(1, 6)); // [output] elax,
console.log(userSlog.slice(-4, -1)); // [output] tim
console.log(userSlog.slice(4)); // [output] x, but work in free time
console.log(userSlog.slice(-4)); // [output] time

// split()

// -------------------------------------------------------------------

// Symbol
let id = Symbol("id");
console.log(id); // [output] Symbol(id)
console.log(typeof id); // [output] symbol

// -------------------------------------------------------------------

// Object
let userInfo = {
    // field
    name: 'Kostya',
    age: 18
}
console.log(userInfo); // [output] {name: 'Kostya', age: 18}
console.log(typeof userInfo); // [output] object

// -------------------------------------------------------------------


