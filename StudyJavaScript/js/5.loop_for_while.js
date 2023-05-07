// while(true) {
//     // code
// }

let num = 5;

while(num) {
    console.log(num); // [output] 5, 4, 3, 2, 1
    num--;
}

while(num) console.log(num--);

num = 0;

do {
    console.log(num); // [output] 0
    num++;
} while(num < 0)

// -------------------------------------------------------------------

// for(start; conditional, end)

for(let i = 0; i < 10; i++) {
    console.log(i); // [output] 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
}

let i;

for(i = 0; i < 10; i++) {
    console.log(i); // [output] 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
}

i = 0;

for(; i < 10;) {
    console.log(i); // [output] 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    i++
}

// break
// continue

// firstFor - note(metka)
firstFor: for(let i = 0; i < 5; i++) {
    for(let j = 0; j < 10; j++) {
        if(j == 3) break firstFor; // stop firstFor with i
        console.log('i = ' + i + ', j = ' + j); // [output] i = 0, j = 0; i = 0, j = 1; i = 0, j = 2 
    }
}

// continue firstFor - like for break








