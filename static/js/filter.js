function validateInput(input) {
    input.value = input.value.replace(/[^A-Za-zא-ת ]/g, '');
}

function trimInput(input) {
    input.value = input.value.trim();
}

function validateID(input) {
    input.value = input.value.replace(/[^\d]/g, '');
}