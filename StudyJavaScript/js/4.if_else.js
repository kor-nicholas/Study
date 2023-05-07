let message = 'Hello, freelancer';

let first = 5;
let second = 10;

if(first === second) {
    console.log(message);
} else if(2 > 1) {
    console.log('True'); // [output] True
} else {
    console.log('Error');
}

if(2 > 1) console.log(message); // [output] Hello, freelancer

message = 'Hello';
let messageEnd;

// if(5 > 1) {
//     messageEnd = ', Vasya';
// } else {
//     messageEnd = ', Olya';
// }

messageEnd = 5 > 1 ? ', Vasya' : ', Olya';

message += messageEnd;
console.log(message); // [output] Hello, Vasya

message = 'Hello';

messageEnd = 5 > 10 ? ', Vasya' :
    5 > 30 ? ', Olya' :
        5 > 10 ? ', Misha' :
            5 > 15 ? ', Andrey' : ', Innokentiy';

message += messageEnd;
console.log(message); // [output] Hello, Innokentiy



