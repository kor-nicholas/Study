let userInfo = new Object();
let userInfo2 = {};

// key -> symbol or string

let firstPart = 'likes';
userInfo = {
    name: 'Kostya',
    age: 20,
    [firstPart + " javascript"]: true,
    0: 'test'
};

console.log(userInfo); // [output] {name: 'Kostya', age: 20}
console.log(userInfo.name); // [output] Kostya
console.log(userInfo['age']); // [output] 20
console.log(userInfo[firstPart + " javascript"]); // [output] true
console.log(userInfo[0]); // [output] test
console.log(userInfo['0']); // [output] test

// -------------------------------------------------------------------

// Symbol - type of data for id

let id = Symbol('id');
userInfo2 = {
    [id]: 'new data',
    address: {
        city: 'city',
        street: 'street',
    }
};

console.log(userInfo2[id]); // [output] new data

function createUser(name, age) {
    return {
        name: name,
        age: age,
        // or
        name, // name = name: name
        age, // age = age: age
    };
}
let user = createUser('Vasya', 20);
console.log(user); // [output] {name: 'Vasya', age: 20}

// Add field
userInfo[id] = 'new data';
userInfo.address = {
    city: 'city',
    street: 'street',
};
userInfo.newUser = userInfo2;

console.log(userInfo); // [output] {0: 'test', name: 'Kostya', age: 20, likes javascript: true, address: {city: 'city', street: 'street'}, newUser: {address: {city: 'city', street: 'street', Symbol(id): 'new data'}, Symbol(id): 'new data'}

Object.assign(userInfo, {test: 'test'});

console.log(userInfo); // [output] (all object) + test: 'test'

// Delete field
delete userInfo[id];
delete userInfo.address;
delete userInfo.newUser;

console.log(userInfo); // [output] 0: 'test', name: 'Kostya', age: 20, likes javascript: true

// Change field

userInfo.age = 100;
console.log(userInfo.age); // [output] 100

// Copy object (copy link for object, not copy object)
// if we change object in copy link - we change in object too

let newUser = userInfo;
newUser.name = 'Zhenya';
console.log(userInfo.name); // [output] Zhenya

// Copy all object
// Object.assign(where we copy, what we copy: all object or some fields)

newUser = Object.assign({}, userInfo);
newUser.name = 'Abrakadabra';
console.log(newUser.name); // [output] Abrakadabra
console.log(userInfo.name); // [output] Zhenya

// Optional (zepochka)

// userInfo.add = {
//     id: 1,
//     text: 'test',
// };

console.log(userInfo?.add?.text); // [output] undefined (not error)

// Operator IN (use when we need check field: undefined)

if('add' in userInfo) {
    console.log(userInfo.add);
} else {
    console.log('Havn\'t add'); // [output] Havn't add
} 

// Loop For IN

for(let key in userInfo) {
    console.log(key); // [output] 0, name, age, likes javascript, test
    console.log(userInfo[key]); // [output] test, Zhenya, 100, true, test
}

// Methods for object

userInfo.showInfo = function() {
    let info = 'User: ';
    for(let key in userInfo) {
        info += `\n${key} = ${userInfo[key]}`;
    }
    console.log(info);
}
userInfo.showInfo();
/*
[output]
User: 
0 = test
name = Zhenya
age = 100
likes javascript = true
test = test
showInfo = function() {
    let info = 'User: ';
    for(let key in userInfo) {
        info += `\n${key} = ${userInfo[key]}`;
    }
    console.log(info);
}
*/

// or

userInfo = {
    name: 'Kostya',
    age: 20,
    showInfo() {
        console.log(`UserInfo: \nname = Kostya\nage = 20`);
    },
}
userInfo.showInfo();
/*
[output]
UserInfo: 
name = Kostya
age = 20
*/

// this (better then just use name or link for object)

// Function-Constructor
// CamelCase, use new

function UserInfo(name) {
    // this = {};

    this.name = name;
    this.age = 24;

    // return this;
}

console.log(new UserInfo('Kostya')); // [output] {name: 'Kostya', age: 24}
console.log(new UserInfo('Vasya')); // [output] {name: 'Vasya', age: 24}


