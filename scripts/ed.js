// JavaScript Text Editor Application

let currentLine = 0;
let fileSaved = false;
let textLines = [];
const textArea = document.getElementById('textArea');
const commandInput = document.getElementById('commandInput');
const fileInput = document.getElementById('fileInput');

// Function to process user commands
function processCommand() {
    const command = commandInput.value.trim();
    commandInput.value = ''; // Clear input field

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
                // Load file from the file input
                loadFile();
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

// Function to set the command in the input field
function setCommand(command) {
    commandInput.value = command;
    commandInput.focus();
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
