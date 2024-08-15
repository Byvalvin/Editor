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

    const [cmd, ...params] = command.split(/\s+/);

    try {
        switch (cmd) {
            case 'p':
                printLines(params[0]);
                break;
            case 'a':
                addLine(params[0]);
                break;
            case 'd':
                deleteLine(params[0]);
                break;
            case 'i':
                insertLine(params[0]);
                break;
            case 'l':
                showFileInput(); // Show file input when loading a file
                break;
            case 'r':
                replaceText(params[0], params[1]);
                break;
            case 's':
                sortLines();
                break;
            case 'w':
                saveFile(params[0]);
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
        // Add cases for other commands if needed
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
        };
        reader.readAsText(file);
    } else {
        alert('No file selected.');
    }
}

// Function to print lines based on the offset
function printLines(offset) {
    if (offset) {
        offset = parseInt(offset, 10);
        const linesToShow = textLines.slice(currentLine, currentLine + offset);
        textArea.textContent = linesToShow.join('\n');
    } else {
        textArea.textContent = textLines[currentLine] || '';
    }
}

// Function to add a new line
function addLine(text) {
    textLines.splice(currentLine + 1, 0, text);
    updateTextArea();
}

// Function to delete a line
function deleteLine(offset) {
    offset = parseInt(offset, 10);
    textLines.splice(currentLine + offset, 1);
    updateTextArea();
}

// Function to insert a new line
function insertLine(text) {
    textLines.splice(currentLine, 0, text);
    updateTextArea();
}

// Function to replace text in lines
function replaceText(find, replace) {
    textLines = textLines.map(line => line.replace(find, replace));
    updateTextArea();
}

// Function to sort lines
function sortLines() {
    textLines.sort();
    updateTextArea();
}

// Function to save the file (not implemented)
function saveFile(filename) {
    alert('Saving files is not implemented yet.');
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
