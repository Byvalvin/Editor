// JavaScript Text Editor Application

let currentLine = 0;
let fileSaved = false;
let textLines = [];
const textArea = document.getElementById('textArea');
const commandInput = document.getElementById('commandInput');

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
                loadFile(params[0]);
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

function setCommand(command) {
    commandInput.value = command;
    commandInput.focus();
}

function printLines(offset) {
    if (offset) {
        offset = parseInt(offset, 10);
        const linesToShow = textLines.slice(currentLine, currentLine + offset);
        textArea.textContent = linesToShow.join('\n');
    } else {
        textArea.textContent = textLines[currentLine] || '';
    }
}

function addLine(text) {
    textLines.splice(currentLine + 1, 0, text);
    updateTextArea();
}

function deleteLine(offset) {
    offset = parseInt(offset, 10);
    textLines.splice(currentLine + offset, 1);
    updateTextArea();
}

function insertLine(text) {
    textLines.splice(currentLine, 0, text);
    updateTextArea();
}

function loadFile(filename) {
    // Placeholder for loading file logic
    alert('Loading files is not implemented yet.');
}

function replaceText(find, replace) {
    textLines = textLines.map(line => line.replace(find, replace));
    updateTextArea();
}

function sortLines() {
    textLines.sort();
    updateTextArea();
}

function saveFile(filename) {
    // Placeholder for saving file logic
    alert('Saving files is not implemented yet.');
    fileSaved = true;
}

function quit() {
    if (!fileSaved) {
        const confirmSave = confirm("Current text not saved. File will be discarded. Do you wish to continue?");
        if (!confirmSave) return;
    }
    // Logic to quit the application
    alert('Quitting application.');
}

function updateTextArea() {
    textArea.textContent = textLines.join('\n');
}
