// Forms

// get all live forms in page (if add new form with js - this find too)
console.log(document.forms); // [output] HTMLCollection(2) [form, form]

// get all const forms in page
console.log(document.querySelectorAll('form')); // [output] NodeList(2) [form, form] 

// get one form
let firstForm = document.forms[0];
let seconfForm = document.forms[1];

// get one form (in html for form set attribute 'name')
firstForm = document.forms.get;
seconfForm = document.forms.post;

console.log(firstForm); // [output] form (get)
console.log(seconfForm); // [output] form (post)

// get all elements for form
console.log(firstForm.elements); // [output] HTMLFormControlsCollection(2) [inout, button]

// get one element from form (need set attribute 'name')
console.log(firstForm.elements.nameInput); // [output] <input type="text" name="nameInput">
console.log(firstForm.nameInput); // [output] <input type="text" name="nameInput">
// if it's type="radio" - return collection with all data

// get parent
console.log(firstForm.nameInput.form); // [output] <form name="get" action="#" mathod="get">...</form> 

// get value from input and textarea
console.log(firstForm.nameInput.value); // [output] input
console.log(firstForm.textarea.value); // [output] bigtext

// set new value in form
firstForm.nameInput.value = 'new text for input or small text';
firstForm.textarea.value = 'new bigtext for textarea';

// get radio, checkbox, file
console.log(firstForm.radio[0].value); // [output] Radio1 ('on' if value="")
console.log(firstForm.radio[1].value); // [output] Radio2 ('on' if value="")
console.log(firstForm.radio[0].checked); // [output] true
console.log(firstForm.radio[1].checked); // [output] false

console.log(firstForm.checkbox.value); // [output] on (because value="")
console.log(firstForm.checkbox.checked); // [output] false

console.log(firstForm.file.value); // [output] '' (because file not choose)
console.log(firstForm.file.files[0]); // [output] undefined (because file not choose)

// set radio, checkbox, file
firstForm.radio[0].value = 'new value for radio';
firstForm.radio[1].checked = true;

firstForm.checkbox.value = 'new value for checkbox';
firstForm.checkbox.checked = true;

firstForm.file.value = ''; // we can only clear file, set - can't

// select and option

// get all options
console.log(firstForm.select.options); // [output] HTMLOptionsCollection(3) [option, option, option, selectedIndex: 2]
// get index of options, that selected
console.log(firstForm.select.selectedIndex); // [output] 2
// get value for option, that selected
console.log(firstForm.select.value); // [output] select3
// get text for option. that selected
console.log(firstForm.select.options[firstForm.select.selectedIndex].text); // [output] 3

// options:
// option.selected - true/false
// option.index - index for option in collection with other options
// option.text - text for option

// set select and option
firstForm.select.options[0].selected = true; // select new option(select1, text = 1)
firstForm.select.selectedIndex = 2; // select new option(select2, text = 2)
firstForm.select.value = 'select3'; // select new option(select3, text = 3)

// add new option
let newOption = new Option('new text for user', 'new value', true, true); // true - attribute selected, true - selected
firstForm.select.append(newOption);
console.log(firstForm.select); // [output] select (with 4 options)

// multiple for select
let selectedOptions = Array.from(firstForm.selectMultiple)
    .filter(option => option.selected)
    .map(option => option.value);

// velues for all selected options
console.log(selectedOptions); // [output] (2) ['1', '4']

// Events

// focus - when we focus for element
// blur - when we unfocus for element

firstForm.addEventListener('focus', function(event) {
    firstForm.nameInput.placeholder = '';
});
firstForm.addEventListener('blur', function(event) {
    console.log('User inputed name');
});

firstForm.textarea.focus(); // focus for element

setTimeout(() => {
    firstForm.textarea.blur();
}, 3000); // wait 3 sec, focus turn off

// get current element, where focus
console.log(document.activeElement); // [output] <textarea name="textarea">bigtext</textarea>

// change - after end change element
// in input -> when finish write text
firstForm.nameInput.addEventListener('change', function(event) {
    console.log('Event change in input');
});
// in select -> when select option
firstForm.select.addEventListener('change', function(event) {
    console.log('Event change in select');
});
// in file -> when load file 
firstForm.file.addEventListener('change', function(event) {
    console.log('Events change in file');
});
// firstForm.radio.addEventListener('change', function(event) {
//     console.log('Event change in radio');
// }); // error
// in checkbox -> when set/unset checkbox
firstForm.checkbox.addEventListener('change', function(event) {
    console.log('Event change in checkbox');
});

// input - when change text in input (every symbol)
firstForm.textarea.addEventListener('input', function(event) {
    console.log(`Value: ${firstForm.textarea.value}`);
});

// last example in textarea
const txtItem = firstForm.textarea;
const txtItemList = txtItem.getAttribute('maxlength');
const txtCounter = document.querySelector('.textarea__counter span');
txtCounter.innerHTML = txtItemList;

txtItem.addEventListener('input', txtSetCounter);

function txtSetCounter() {
    const txtCounterResult = txtItemList - txtItem.value.length;
    txtCounter.innerHTML = txtCounterResult;
};

// cut, copy, paste - events
firstForm.nameInput.addEventListener('copy', function(event) {
    console.log(`Copy: ${event.value}`);
});
firstForm.nameInput.addEventListener('cut', function(event) {
    console.log(`Cut: ${event.value}`);
    // event.preventDefault(); // turn off cut
});
firstForm.nameInput.addEventListener('paste', function(event) {
    console.log(`Paste: ${event.value}`);
});

// submit - send data from form (button 'submit', input 'submit', Enter)
firstForm.addEventListener('submit', function(event) {
    console.log('Check forms ...');

    if(!firstForm.nameInput.value) {
        console.log('Error: Write text in name');
        event.preventDefault(); // turn off send form
    }
});

// or

if(firstForm.nameInput.value === 'send') {
    firstForm.submit();
};

// example 1

seconfForm.addEventListener('submit', function(event) {
    if(emailTest(seconfForm.nameInput)) {
        seconfForm.nameInput.parentElement.insertAdjacentHTML(
            'beforeend',
            `<div style="color: red">
                Error: Enter email
            </div>`
        );
        event.preventDefault();
    }
});

seconfForm.nameInput.addEventListener('focus', function(event) {
    if(seconfForm.nameInput.nextElementSibling) {
        seconfForm.nameInput.nextElementSibling.remove();
    }
});

function emailTest(input) {
    return !/^\W+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,8})+$/.test(input.value);
}

// example 2

seconfForm.file.addEventListener('change', function(event) {
    let selectedFile = seconfForm.file.files[0];

    let fileUrl = URL.createObjectURL(selectedFile);

    seconfForm.file.parentElement.insertAdjacentHTML(
        'beforeend',
        `<img alt="Picture not found" title="${selectedFile.name}" src="${fileUrl}">`
    );
});








