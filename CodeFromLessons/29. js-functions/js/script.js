//ДОМАШКА
/*
1. Изучить теорию
2. Решить задачи:


// Задача №1
// Кто попадет в консоль первым Вася или Коля?
function showName() {
	console.log('Вася!');
}
setTimeout(showName, 0);
console.log('Коля!');

// Задача №2
// Верно ли вызвана функция
showMessage();
function showMessage() {
	console.log('Сообщение');
}
// Задача №3
// Верно ли вызвана функция
showMessage();
let showMessage = function () {
	console.log('Сообщение');
}
// Задача №4
// Как решить проблему?
'use strict'
if (2 > 1) {
	function showMessage() {
		console.log('Сообщение');
	}
}
showMessage(); // Error (showMessage is not defined)

*/

//========================================================================================================================================================
//========================================================================================================================================================
//Объявление функции (Function Declaration)
/*
function имя(параметры) {
	// тело (код) функции
}*/
//===========================================================

//Имя функции и её предназначение
/*
Как правило, в имени используются опеределенные префиксы,
обозначающие действие, после которых следует объект действия.

Например, функции, начинающиеся с
"show..." обычно что-то показывают,
"get..." – возвращают значение,
"calc..." – что-то вычисляют,
"create..." – что-то создают,
"check..." – что-то проверяют и возвращают логическое
значение, и т.д.

Примеры:
showMessage - показать сообщение
getOptions - получить параметры
calcSum - посчитать сумму
и т.д.
*/

// Функция вывода сообщения
/*
function showMessage() {
	console.log('Сообщение');
}
*/

/*
Функция должна делать только то,
что явно подразумевается её названием.
И это должно быть одним действием.
Два независимых действия обычно подразумевают две функции,
даже если предполагается, что они будут вызываться вместе (в этом случае мы
можем создать третью функцию, которая будет их вызывать).
*/

//===========================================================
//Запуск функции
/*
showMessage();

// Функция вывода сообщения
function showMessage() {
	console.log('Сообщение!');
}
showMessage();
showMessage();
*/

//===========================================================

/*
function getSumm() {
	let numOne, numTwo;

	function getNumOne() {
		numOne = 1;
	}
	function getNumTwo() {
		numTwo = 2;
	}
	getNumOne();
	getNumTwo();

	let numSumm = numOne + numTwo;
	console.log(numSumm);
}
getNumOne();
getSumm();
*/
//-----
/*
// Вложенность и видимость функций
"use strict"
if (2 > 1) {
	function getSumm() {
		let numOne, numTwo;

		function getNumOne() {
			numOne = 1;
		}
		function getNumTwo() {
			numTwo = 2;
		}
		getNumOne();
		getNumTwo();

		let numSumm = numOne + numTwo;
		console.log(numSumm);
	}
}
getSumm();
*/
//===========================================================
//Локальные и внешние переменные
/*
function showMessage() {
	// Локальная переменная
	let message = "Сообщение";
	console.log(message);
}

console.log(message);
*/

//-----
/*
// Внешняя переменная
let message;

function showMessage() {
	// Используется внешняя переменная
	message = "Сообщение";
}
console.log(message);

showMessage();
*/

//-----

/*
// Внешняя переменная
let message = "Сообщение №1";

function showMessage() {
	// Локальная переменная
	let message = "Сообщение №2";
	console.log(message);
}
console.log(message);
showMessage();

*/
//------

/*
// Глобальные переменные
let globalVar = "Я глобальная переменная";

function getSumm() {
	let numOne, numTwo;

	function getNumOne() {
		numOne = 1;
		console.log(globalVar);
	}
	function getNumTwo() {
		numTwo = 2;
	}
	getNumOne();
	getNumTwo();

	let numSumm = numOne + numTwo;
	console.log(globalVar);
}
console.log(globalVar);

getSumm();
*/

//===========================================================
/*
// Параметры (аргументы)
function calcSumm(numOne = 1, numTwo = 2) {
	console.log(`Переменная numOne:${numOne}`);
	console.log(`Переменная numTwo:${numTwo}`);

	let numSumm = numOne + numTwo;

	console.log(`Сумма:${numSumm}`);
}

calcSumm(5, 5);
*/



//------
/*
numTwo = numTwo || 2;
*/

/*
// Функции-колбэки
function calcSumm(numOne, numTwo, more, less) {
	let numSumm = numOne + numTwo;

	if (numSumm > 3) {
		more();
	} else {
		less();
	}
}

function showMoreMessage() {
	console.log('Больше чем 3');
}
function showLessMessage() {
	console.log('Меньше чем 3');
}
calcSumm(1, 1, showMoreMessage, showLessMessage);
*/

//===========================================================

/*
// Возврат результата
function calcSumm(numOne, numTwo) {

	let numSumm = numOne + numTwo;

	// Возврат
	return numSumm;

	// Дальше код не выполняется

}
let funcRezult = calcSumm(1, 2);

console.log(`Сумма: ${funcRezult}`);
*/

//------
/*
function calcSumm(numOne, numTwo) {

	let numSumm = numOne + numTwo;

	if (numSumm >= 3) {
		// Возврат
		return numSumm;
	} else {
		return 'Сумма меньше 3';
	}
	// Дальше код не выполняется

}
let funcRezult = calcSumm(1, 2);

console.log(funcRezult);
*/

//------
/*
function calcSumm(numOne, numTwo) {

	let numSumm = numOne + numTwo;

	return
	numSumm;

	// Дальше код не выполняется

}
let funcRezult = calcSumm(1, 2);

console.log(funcRezult);
*/
//------
/*
function calcSumm(numOne, numTwo) {

	let numSumm = numOne + numTwo;

	if (numSumm >= 3) {
		// Возврат
		return;
		// Дальше код не выполняется
	}
}
calcSumm(5, 5)
*/
//===========================================================
// Рекурсия
/*
function getSumm(numOne, numTwo) {
	let numSumm = calcSumm(numOne, numTwo);

	console.log(numSumm);
}
function calcSumm(numOne, numTwo) {
	return numOne + numTwo;

}
getSumm(5, 5);
*/

//------
/*
function calcSumm(numOne, numTwo) {
	let result = 1;
	// умножаем result на numOne numTwo раз в цикле
	for (let i = 0; i < numTwo; i++) {
		result *= numOne;
	}
	return result;
}
console.log(calcSumm(2, 3));
*/

//------
/*
function calcSumm(numOne, numTwo) {
	if (numTwo === 1) {
		return numOne;
	} else {
		return numOne * calcSumm(numOne, numTwo - 1);
	}
}
console.log(calcSumm(2, 3));
*/

//========================================================================================================================================================
/*
let showMessage = function () {
	console.log('Привет!');
};

showMessage();
*/
//-----
/*
function getSumm() {
	let summ = 1 + 2;
	console.log(summ);
};

let someVar = getSumm;

someVar();
getSumm();

*/
//-----
/*
//Объявление функции (Function Declaration)
function getSumm() {
	let summ = 1 + 2;
	console.log(summ);
};
getSumm();

// Функциональное выражение (Function Expression)
let showMessage = function () {
	console.log('Привет!');
};
showMessage();
*/

//-----
/*
'use strict'
if (2 > 1) {
	function getSumm() {
		let summ = 1 + 2;
		console.log(summ);
	};
}
getSumm();
*/
/*
let getSumm;

if (2 > 1) {
	getSumm = function () {
		let summ = 1 + 2;
		console.log(summ);
	};
}
getSumm();
*/
//===========================================================
//Функции стрелки(arrow functions)
/*
// Функциональное выражение (Function Expression)
let имя переменной = function (параметр, ...параметр) {
	return выражение;
};

// Cтрелочная функция (arrow function)
let имя переменной = (параметр, ...параметр) => выражение
*/
//-----

// Однострочная стрелочная функция
/*
let getMessage = (text, name) => text + ', ' + name + '!';
console.log(getMessage('Привет', 'Вася'));


// Многострочная стрелочная функция
let getMessage = (text, name) => {
	let message = text + ', ' + name + '!';
	return message;
};
console.log(getMessage('Привет', 'Вася'));
*/
//===========================================================
// Планирование setTimeout и setInterval
/*
Что бы реализовать планирование существуют два метода:
1.	setTimeout позволяет вызвать функцию один раз
	через определённый интервал времени
2.	setInterval позволяет вызывать функцию регулярно,
	повторяя вызов через определённый интервал времени.
*/
/*
setTimeout(функция или код, задержка, параметр, ...параметр);
setInterval(функция или код, задержка, параметр, ...параметр);
*/
/*
function showMessage(text, name) {
	console.log(`${text}, ${name}!`);
	setTimeout(showMessage, 500, text, name);
}
//setInterval(showMessage, 500, 'Привет', 'Вася');
setTimeout(showMessage, 500, 'Привет', 'Вася');
*/
//---
/*
let result = 0;
function showNumber(num) {
	result += num;
	console.log(result);
	if (result === 5) {
		clearInterval(timeId);
	}
}
let timeId = setInterval(showNumber, 1000, 1);
*/
//---
/*
setTimeout(function () {
	console.log('Привет!');
}, 1000);

setTimeout(() => {
	console.log('Привет!');
}, 1000);
*/

//----
/*
function showMessageOne() {
	console.log("А я первый!");
}
function showMessageTwo() {
	console.log("А я второй(");
}

setTimeout(showMessageTwo, 0);

showMessageOne();

*/
//===========================================================
/*
// Применение функций

// Функция соединения строк
function createMassage(text, name) {
	return `${text}, ${name}!`;
}
// Функция вывода в консоль
function showMassage(message) {
	console.log(message);
}
// Объединяющая функция, вызывает обе функции
function initMessage(text, name) {
	showMassage(createMassage(text, name));
}

initMessage('Привет', 'Фрилансер');

*/
//========================================================================================================================================================
//========================================================================================================================================================
