// JavaScript Text Editor Application

let currentLine = 0;
let fileSaved = false;
let textLines = [];
const textArea = document.getElementById('textArea');
const commandInput = document.getElementById('commandInput');
const fileInput = document.getElementById('fileInput');
const additionalInputs = document.getElementById('additionalInputs');

// Function to process user commands
function processCommand() {
    const command = commandInput.value.trim();
    commandInput.value = ''; // Clear input field
    additionalInputs.innerHTML = ''; // Clear additional inputs

    if (!command) return; // Ignore empty commands

    const [cmd] = command.split(/\s+/);

    try {
        switch (cmd) {
            case 'p':
                printLines();
                break;
            case 'a':
                addLine();
                break;
            case 'd':
                deleteLine();
                break;
            case 'i':
                insertLine();
                break;
            case 'r':
                replaceText();
                break;
            case 'l':
                loadFile();
                break;
            case 's':
                sortLines();
                break;
            case 'w':
                saveFile();
                break;
            case 'q':
                quit();
                break;
            default:
                throw new Error(`Unknown command: ${cmd}`);
        }
    } catch (error) {
        alert(`Error: ${error.message}`);
    }
}

// Function to set the command in the input field and create additional inputs if needed
function setCommand(command) {
    commandInput.value = command;
    commandInput.focus();
    createAdditionalInputs(command);
}

// Function to create additional input fields based on the command
function createAdditionalInputs(command) {
    additionalInputs.innerHTML = ''; // Clear existing inputs

    // Hide the file input field initially
    fileInput.style.display = 'none';

    switch (command) {
        case 'p':
            createInputField('offset', 'Number of lines to print (or leave empty for current line)');
            break;
        case 'a':
            createInputField('text', 'Text to add');
            break;
        case 'd':
            createInputField('offset', 'Line number to delete');
            break;
        case 'i':
            createInputField('text', 'Text to insert');
            break;
        case 'r':
            createInputField('find', 'Text to find');
            createInputField('replace', 'Text to replace with');
            break;
        case 'w':
            createInputField('filename', 'Filename to save');
            break;
        case 'l':
            showFileInput(); // Show file input when loading a file
            break;
    }
}

// Function to create an individual input field
function createInputField(id, placeholder) {
    const input = document.createElement('input');
    input.type = 'text';
    input.id = id;
    input.placeholder = placeholder;
    additionalInputs.appendChild(input);
}

// Function to show the file input field
function showFileInput() {
    fileInput.style.display = 'block';
}

// Function to handle file input
function loadFile() {
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            const fileContent = event.target.result;
            textLines = fileContent.split('\n');
            updateTextArea();
            fileSaved = true; // Mark file as saved after loading
        };
        reader.readAsText(file);
    } else {
        alert('No file selected.');
    }
}

// Function to print lines based on the offset
function printLines() {
    const offset = document.getElementById('offset')?.value.trim();
    if (offset) {
        const numLines = parseInt(offset, 10);
        if (isNaN(numLines) || numLines <= 0) throw new Error('Invalid offset.');
        const linesToShow = textLines.slice(currentLine, currentLine + numLines);
        textArea.textContent = linesToShow.join('\n');
    } else {
        textArea.textContent = textLines[currentLine] || '';
    }
}

// Function to add a new line
function addLine() {
    const text = document.getElementById('text')?.value.trim();
    if (!text) throw new Error('No text provided.');
    textLines.splice(currentLine + 1, 0, text);
    updateTextArea();
}

// Function to delete a line
function deleteLine() {
    const offset = document.getElementById('offset')?.value.trim();
    const lineOffset = parseInt(offset, 10);
    if (isNaN(lineOffset) || lineOffset < 1 || currentLine + lineOffset - 1 >= textLines.length) throw new Error('Invalid line number.');
    textLines.splice(currentLine + lineOffset - 1, 1);
    updateTextArea();
}

// Function to insert a new line
function insertLine() {
    const text = document.getElementById('text')?.value.trim();
    if (!text) throw new Error('No text provided.');
    textLines.splice(currentLine, 0, text);
    updateTextArea();
}

// Function to replace text in lines
function replaceText() {
    const find = document.getElementById('find')?.value.trim();
    const replace = document.getElementById('replace')?.value.trim();
    if (!find || !replace) throw new Error('Find and replace texts are required.');
    textLines = textLines.map(line => line.replace(new RegExp(find, 'g'), replace));
    updateTextArea();
}

// Function to sort lines
function sortLines() {
    textLines.sort();
    updateTextArea();
}

// Function to save the file
function saveFile() {
    const filename = document.getElementById('filename')?.value.trim();
    if (!filename) throw new Error('Filename is required.');
    const blob = new Blob([textLines.join('\n')], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
    fileSaved = true;
}

// Function to quit the application
function quit() {
    if (!fileSaved) {
        const confirmSave = confirm("Current text not saved. File will be discarded. Do you wish to continue?");
        if (!confirmSave) return;
    }
    alert('Quitting application.');
}

// Function to update the text area
function updateTextArea() {
    textArea.textContent = textLines.join('\n');
}

// Event listener for file input change
fileInput.addEventListener('change', loadFile);
