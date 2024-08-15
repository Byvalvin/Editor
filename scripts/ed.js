// ed.js
let textFile = {
    content: "",
    filename: "new.txt",
};

// Show input fields based on command
function showInput(command) {
    const inputSection = document.getElementById('input-section');
    inputSection.innerHTML = ''; // Clear previous inputs

    switch (command) {
        case 'a': // Add Text
        case 'i': // Insert Text
            inputSection.innerHTML += '<input type="text" id="text-input" placeholder="Enter text here">';
            break;

        case 'd': // Delete Line
            inputSection.innerHTML += '<input type="text" id="line-number" placeholder="Enter line number to delete">';
            break;

        case 'l': // Load File
            inputSection.innerHTML += '<input type="file" id="file-input" accept=".txt">';
            break;

        case 'p': // Print Line
            inputSection.innerHTML += '<input type="text" id="print-line-number" placeholder="Enter line number to print">';
            break;

        case 'r': // Replace Text
            inputSection.innerHTML += '<input type="text" id="old-text" placeholder="Text to replace">';
            inputSection.innerHTML += '<input type="text" id="new-text" placeholder="New text">';
            break;

        case 's': // Sort Lines
            // No additional input needed for sorting
            break;

        case 'w': // Save File
            // No additional input needed for saving
            break;

        case '/': // Search Forward
        case '?': // Search Backward
            inputSection.innerHTML += '<input type="text" id="search-text" placeholder="Enter text to search">';
            break;

        default:
            break;
    }

    // Add a submit button to handle the command
    inputSection.innerHTML += '<button onclick="executeCommand(\'' + command + '\')">Submit</button>';
}

function executeCommand(cmd) {
    const outputElement = document.getElementById('output');
    let parameters = '';
    
    switch (cmd) {
        case 'a': // Add text
        case 'i': // Insert text
            parameters = document.getElementById('text-input')?.value;
            break;

        case 'd': // Delete line
            parameters = document.getElementById('line-number')?.value;
            break;

        case 'l': // Load file
            const fileInput = document.getElementById('file-input');
            if (fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const reader = new FileReader();
                reader.onload = function(e) {
                    textFile.content = e.target.result;
                    outputElement.innerHTML += `File loaded: ${file.name}<br>`;
                };
                reader.readAsText(file);
            }
            return;

        case 'p': // Print lines
            parameters = document.getElementById('print-line-number')?.value;
            break;

        case 'r': // Replace text
            const oldText = document.getElementById('old-text')?.value;
            const newText = document.getElementById('new-text')?.value;
            parameters = `${oldText} ${newText}`;
            break;

        case '/': // Search forward
        case '?': // Search backward
            parameters = document.getElementById('search-text')?.value;
            break;

        default:
            break;
    }

    handleCommand(cmd, parameters);
}

function handleCommand(cmd, parameters) {
    const outputElement = document.getElementById('output');
    const args = parameters ? parameters.split(/\s+/) : [];

    switch (cmd) {
        case 'a': // Add text
            textFile.content += args.join(' ') + '\n';
            break;

        case 'd': // Delete line
            const deleteIndex = parseInt(args[0], 10);
            if (!isNaN(deleteIndex)) {
                textFile.content = textFile.content.split('\n').filter((_, i) => i !== deleteIndex).join('\n');
            }
            break;

        case 'i': // Insert text
            const insertIndex = parseInt(args[0], 10);
            if (!isNaN(insertIndex)) {
                const lines = textFile.content.split('\n');
                lines.splice(insertIndex, 0, args.slice(1).join(' '));
                textFile.content = lines.join('\n');
            }
            break;

        case 'p': // Print lines
            const printIndex = parseInt(args[0], 10);
            if (!isNaN(printIndex)) {
                const lines = textFile.content.split('\n');
                if (printIndex < lines.length) {
                    outputElement.innerHTML += `Line ${printIndex}: ${lines[printIndex]}<br>`;
                }
            }
            break;

        case 'r': // Replace text
            const [oldText, newText] = args;
            textFile.content = textFile.content.replace(new RegExp(oldText, 'g'), newText);
            break;

        case 's': // Sort lines
            textFile.content = textFile.content.split('\n').sort().join('\n');
            break;

        case 'w': // Save file
            const filename = prompt("Enter filename:", textFile.filename);
            if (filename) {
                const blob = new Blob([textFile.content], { type: 'text/plain' });
                const link = document.createElement('a');
                link.href = URL.createObjectURL(blob);
                link.download = filename;
                link.click();
                textFile.filename = filename;
            }
            break;

        case '/': // Search forward
        case '?': // Search backward
            const searchText = args[0];
            const lines = textFile.content.split('\n');
            let found = false;
            if (cmd === '/') { // Search forward
                for (const line of lines) {
                    if (line.includes(searchText)) {
                        outputElement.innerHTML += `Found: ${line}<br>`;
                        found = true;
                        break;
                    }
                }
            } else if (cmd === '?') { // Search backward
                for (let i = lines.length - 1; i >= 0; i--) {
                    if (lines[i].includes(searchText)) {
                        outputElement.innerHTML += `Found: ${lines[i]}<br>`;
                        found = true;
                        break;
                    }
                }
            }
            if (!found) {
                outputElement.innerHTML += `Text not found<br>`;
            }
            break;

        default:
            outputElement.innerHTML += `Invalid command: ${cmd}<br>`;
            break;
    }

    outputElement.innerHTML += `Content:<br>${textFile.content.replace(/\n/g, '<br>')}<br>`;
}

function quit() {
    alert("Good-bye");
}
