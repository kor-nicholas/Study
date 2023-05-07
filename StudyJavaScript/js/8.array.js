// Array - it's object
// so... it copy for link (like object)

let arr = new Array();
arr = [];

arr = [
    'test1',
    'test2',
    'test3',
];
// or
arr = ['test1', 'test2', 'test3', ];

arr1 = [
    'Kostya',
    {
        type: '35',
        age: 35,
    },
    true,
    function() {
        console.log('Hello World!');
    },
];

let matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
];

console.log(matrix[0][1]); // [output] 2
console.log(matrix[0][5]); // [output] undefined

arr1[3](); // [output] Hello World!

matrix[0][1] = 100; // change value from 2 to 100
matrix[0][5] = 24; // add new value
delete matrix[0]; // delete value for index, but value -> undefined
matrix[1].splice(1, 2); // delete from 1 index 2 elements

// Methods

// push - add new data in end
arr.push('test4', 'test5');
console.log(arr); // [output] ['test1', 'test2', 'test3', 'test4', 'test5']
// shift - delete first element and 2 -> 1, 3 -> 2, ...
arr.shift();
console.log(arr); // [output] ['test2', 'test3', 'test4', 'test5']
// pop - delete past element
arr.pop();
console.log(arr); // [output] ['test2', 'test3', 'test4']
// unshift - add element/elements in start and change all elements ...
arr.unshift('test45', 'test23');
console.log(arr); // [output] ['test45', 'test23', 'test2', 'test3', 'test4']
// pop/push - quickly, shift/unshift - slowly

// copy
let arrCopy = arr.slice(); // copy all arr
console.log(arrCopy); // [output] ['test45', 'test23', 'test2', 'test3', 'test4']
arrCopy = arr.slice(1, 3); // copy from 1 to 3 index
console.log(arrCopy); // [output] ['test23', 'test2']
arrCopy = arr.slice(1); // copy from 1 index to end
console.log(arrCopy); // [output] ['test23', 'test2', 'test3', 'test4']
// concat('test100') -> create copy, but with new data in end

// indexOf() and includes() -> like string

// find()

arr = [
    {name: 'Kostya', age: 38},
    {name: 'Vasya', age: 20},
    {name: 'Olya', age: 'No say ;)'},
];

// function - work for every element in array
let resultFind = arr.find(function(item, index, array) {
    return item.age === 20;
});
// resultFind = arr.find((item, index, array) => item.age === 20);
console.log(resultFind); // [output] {name: 'Vasya', age: 20}

// findIndex() - like find, but return index for element
// filter() - like find, but not stop when find element and return array of elements
// sort() - numbers for grow(no work, because method convert to string) and strings for alphabet

let arrOfNumbers = [8, 22, 1];

function ourSort(a, b) {
    console.log(`Check: ${a} and ${b}`);
    // if(a > b) return 1;
    // if(a == b) return 0;
    // if(a < b) return -1; 

    return a - b;
}

console.log(arrOfNumbers.sort(ourSort)); // [output] 1, 8, 22
// console.log(arrOfNumbers.sort((a, b) => a - b));

// reverse()

// map() - complete function for all elements and return arr with result

console.log(arrCopy); // [output] ['test23', 'test2', 'test3', 'test4']
let result = arrCopy.map(function(item, index, array) {
    return item[0];
});
// let result = arrCopy.map((item) => item[0]);
console.log(result); // [output] ['t', 't', 't', 't']

// split()
console.log('qq 145 beta'.split(' ')); // [output] ['qq', '145', 'beta']

// join() - create str for delimeter (anti-split)
console.log(arrOfNumbers.join(', ')); // [output] 1, 8, 22

// Array.isArray(arr) - check, array is it or no (because typeof arr -> object)

for(let item of arrOfNumbers) {
    console.log(item); // [output] 1; 8; 22
}

// forEach() -> function for every element in array
arrCopy.forEach(function(item, index, array) {
    console.log(`${item} has index ${index} in ${array}`);
});
// arrCopy.forEach((item, index, array) => console.log(`${item} has index ${index} in ${array}`));
/* [output]
test23 has index 0 in test23,test2,test3,test4
test2 has index 1 in test23,test2,test3,test4
test3 has index 2 in test23,test2,test3,test4
test4 has index 3 in test23,test2,test3,test4
*/

// reduce() - function for every element, but add result in next iteration
// reduce(function(prevValue, item, index, array){return item + prevValue}, 0);
// 0 - initial argument (if we don't use it -> initial argument = first element in array)

// reduceRight() - like reduce, but from right to left








