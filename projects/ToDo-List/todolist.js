const addButton = document.querySelector('.addButton');
var inputValue = document.querySelector('.input');
const container = document.querySelector('.container');

class item {
    constructor(itemName) {
        this.creatediv(itemName);
    }
    creatediv(itemName) {
        let input = document.createElement('input');

        input.value = itemName;
        input.disabled = true;
        input.classList.add('item_input');
        input.type = 'text';

        let itembox = document.createElement('div');
        itembox.classList.add('item');

        let editButton = document.createElement('button');
        editButton.classList.add('editButton');
        editButton.innerHTML = "EDIT";
        let removeButton = document.createElement('button');
        removeButton.classList.add('removeButton');
        removeButton.innerHTML = "REMOVE";
        container.appendChild(itembox);
        itembox.appendChild(input);
        itembox.appendChild(editButton);
        itembox.appendChild(removeButton);


        editButton.addEventListener('click', () => this.edit(input));

        removeButton.addEventListener('click', () => this.remove(itembox));

    }

    edit(input) {

        input.disabled = !input.disabled;

    }
    remove(itembox) {
        container.removeChild(itembox);
    }


}


new item("ENTER WORKS TO DO");


function check() {
    if (inputValue.value != " ") {
        new item(inputValue.value);
    }
    inputValue.value = inputValue.ariaPlaceholder;
}
addButton.addEventListener('click', check)
