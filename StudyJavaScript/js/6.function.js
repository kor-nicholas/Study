
// Function Declaration

function showMessage(params) {
    console.log('message');
}

showMessage(); // [output] message

// showName, getName, calcAge, createGame, checkIp, ...

function getSumm() {
    let numOne, numTwo;

    function setNumOne() {
        numOne = 1;
    }

    function setNumTwo() {
        numTwo = 2;
    }

    setNumOne();
    setNumTwo();

    let summ = numOne + numTwo;
    console.log(summ);
}

getSumm(); // [output] 3

// setNumOne(); // error
// setNumTwo(); // error

function calcSumm(numOne = 1, numTwo = 5) {
    // if numOne or numTwo not set default values -> undefined
    let summ = numOne + numTwo;
    console.log(summ);
}

calcSumm(1, 2); // [output] 3
calcSumm('1', '2'); // [output] 12
calcSumm(); // [output] 6 (use default values)

// Callback-function
function checkSumm(numOne, numTwo, more, less) {
    let summ = numOne + numTwo;

    if(summ > 5) {
        more();
    } else {
        less();
    }
}

function showMoreMessage() {
    console.log('More then 5');
}

function showLessMessage() {
    console.log('Less then 5');
}

checkSumm(1, 5, showMoreMessage, showLessMessage); // [outpput] More then 5

// return (return; -> return undefined)

// Function Expression
// we can use function only after create func (Function Declaration - before or after)

let showMess = function() {
    console.log('first');
}

showMess(); // [output] first

let someVar = showMess;

showMess(); // [output] first
someVar(); // [output] first

if(2 > 1) {
    function getSum() {
        let summ = 1 + 2;
        console.log(summ);
    };
}
getSum(); // [output] 3 (in theory - must be error)

let getSumVar;

if(2 > 1) {
    getSumVar = function() {
        let summ = 1 + 2;
        console.log(summ);
    };
}
getSumVar(); // [output] 3

// Arrow function
let nameVar = function(param1, param2) {
    return param1 + param2;
}

let nameVar2 = (param1, param2) => param1 + param2;

console.log(nameVar(1, 4)); // [output] 5
console.log(nameVar2(1, 3)); // [output] 4

let getMessageVar = (paramHello, paramName) => {
    let message = paramHello + paramName;
    return message;
};

console.log(getMessageVar('Hello', ', Vasya')); // [output] Hello, Vasya

// setTimeout and setInterval
// setTimeout (run func once after interval of time in miliseconds)
// setInterval (run func sometime for interval of time in miliseconds between runs)

let timeId = setTimeout(checkSumm, 3000, 1, 5, showMoreMessage, showLessMessage);
timeId == 3 ? console.log('time = 3') : clearTimeout(timeId); // [output] time = 3; More then 5
timeId = setInterval(checkSumm, 3000, 1, 5, showMoreMessage, showLessMessage);
clearInterval(timeId); // stop interval
timeId == 4 ? console.log(`time = ${timeId}`) : clearInterval(timeId); // [output] time = 4, More then 5; More then 5; ...





