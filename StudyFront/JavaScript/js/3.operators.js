// Operators

// Operand - for this use operators (30 - 6, 30 is operand)
let userAge = 30 - 6; // bynaric (because 2 operand)
userAge = -800; // ynaric (because 1 operand)

// Basic (math)

let x;
x = 5 + 8;
x = 9 - 5;
x = 3 * 4;
x = 10 / 2;
// 3 * 3 = 9, 11 - 9 = 2
x = 11 % 3; // [output] 2
x = 5 ** 3; // [output] 125 (like 5 ^ 3)

let text = 'User age is ' + userAge + 823;
console.log(text); // [output] User age is -800823
console.log(typeof text); // [output] string
text = 'User age is ' + (userAge + 823);
console.log(text); // [output] User age is 23
text = userAge + 823 + ' is User age';
console.log(text); // [output] 23 is User age

let resultOne = '25' - 5;
console.log(resultOne); // [output] 20
console.log(typeof resultOne); // [output] number
let resultTwo = 3 * 'Freelancer';
console.log(resultTwo); // [output] NaN
console.log(typeof resultTwo); // [output] number

resultOne = +'25';
console.log(resultOne); // [output] 25
console.log(typeof resultOne); // [output] number

// increment
let users = 10;
users++;
console.log(users); // [output] 11
// console.log(5++); // [output] error

let usersCounter = 0;
let newUsers = usersCounter++;
console.log(newUsers); // [output] 0
newUsers = ++usersCounter;
console.log(newUsers); // [output] 1

// decrement
users--;
console.log(users); // [output] 10
// console.log(5--); // [output] error

usersCounter = 0;
newUsers = usersCounter--;
console.log(newUsers); // [output] 0
newUsers = --usersCounter;
console.log(newUsers); // [output] -1

// , (complete all, but return last)
usersCounter = (8 + 2, 19 + 1)
console.log(usersCounter); // [output] 20

// For bytes operators
// AND(и) ( & )
// OR(или) ( | )
// XOR(побитовое исключение или) ( ^ )
// NOT(не) ( ~ )
// LEFT SHIFT(левый сдвиг) ( << )
// RIGHT SHIFT(правый сдвиг) ( >> )
// ZERO-FILL RIGHT SHIFT(правый сдвиг с заполнением нулями) ( >>> )

// -------------------------------------------------------------------

// Operator =

let a = 1 + 2;
let b = 2;
let result = 8 - (a = b + 3);
console.log(result); // [output] 3

let one = two = three = 1 + 2;
console.log(one); // [output] 3
console.log(two); // [output] 3
console.log(three); // [output] 3

one += two;
console.log(one); // [output] 6

// -------------------------------------------------------------------

// Logical

// >
// <
// >=
// <=
// ==
// !=
// === (hard =, строгое равно)
// !== (hard !=, строгое не равно)

// for alphabet
console.log('B' > 'A'); // [output] true
console.log('Script' > 'Scripka'); // [output] !!! TODO: ChECK ALPHABET !!!
console.log('Slaider' > 'Slaid'); // [output] true
console.log('Freelancer' > 'freelancer'); // [output] false

console.log('58' > 10); // [output] true
console.log(true > 51); // [output] false

let itemA = 0;
let itemB = '0';

console.log(Boolean(itemA)); // [output] false (because 0 -> false)
console.log(Boolean(itemB)); // [output] true (because str not '')
console.log(itemA == itemB); // [output] true (because js convert in number)

console.log(0 === false); // [output] false (because js not convert in number)
console.log('007' === 7); // [output] false
console.log('58' !== 58); // [output] true

// when convert in number (null = 0, undefiner = NaN)
console.log(null == undefined); // [output] true
console.log(null === undefined); // [output] false
console.log(null > 0); // [output] false
console.log(null == 0); // [output] false
console.log(null >= 0); // [output] true
console.log(undefined > 0); // [output] false
console.log(undefined == 0); // [output] false
console.log(undefined >= 0); // [output] false

// OR ( || )
// if have true - use this variant of true as result, if all false - last

console.log(true || 'text' || 1); // [output] true
console.log(false || true || 1); // [output] true
console.log(false || false || 1); // [output] 1
console.log(false || false || false); // [output] false

console.log(1 || 0); // [output] 1
console.log(true || 'freelancer'); // [output] true
console.log(null || 58); // [output] 58
console.log(null || 'freelancer' || 58); // [output] freelancer
console.log(undefined || '' || null || 0); // [output] 0

let admins = 0;
users = 5;
admins > users || users++;
console.log(users); // [output] 6 (because admins not > users, users++)

// AND ( && )
// if have false - use this variant of false as result, if all true - last
// priority more then ||

console.log(true && 'text' && 1); // [output] 1
console.log(false && true && 1); // [output] false
console.log(true && '' && 1); // [output]  ('' - nothing)
console.log(null && false && 0); // [output] null

(users > 0) && console.log(`Count of users: ${users}`);

// NOT ( ! )
// max priority for AND( && ) and OR( || )

console.log(!true); // [output] false
console.log(!null); // [ouptuy] true
console.log(!1); // [output] false
console.log(!''); // [output] true
console.log(!'freelancer'); // [output] false

// 1. !true -> false
// 2. !1 -> 0 (false)
// 3. false && 50 -> false
// 4. 18 && false -> false
// 5. false || false -> false
console.log(!true && 50 || 18 && !1); // [output] false

console.log(!!'freelancer'); // [output] true (convert in boolean)
console.log(Boolean('freelancer')); // [output] true

// check for null/undefined
// if null/undefined -> 'Without name' else -> name
let name;
console.log(name ?? 'Without name'); // [output] Without name
name = 'Kostya';
console.log(name ?? 'Without name'); // [output] Kostya

// -------------------------------------------------------------------






