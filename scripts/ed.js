// ed.js

let textFile = {
    content: "",
    filename: "new.txt",
};

// Store the last selected command
let selectedCommand = '';

function selectCommand(command) {
    // Remove highlight from all buttons
    document.querySelectorAll('.button-container button').forEach(button => {
        button.classList.remove('selected');
    });

    // Highlight the selected button
    const selectedButton = document.getElementById(`btn-${command}`);
    if (selectedButton) {
        selectedButton.classList.add('selected');
    } else {
        console.error(`Button with ID 'btn-${command}' not found.`);
    }

    // Show input fields based on command
    showInput(command);
    selectedCommand = command; // Update the selected command
}

function showInput(command) {
    const inputSection = document.getElementById('input-section');
    inputSection.innerHTML = ''; // Clear previous inputs

    switch (command) {
        case 'a': // Add Text
        case 'i': // Insert Text
            inputSection.innerHTML += '<input type="text" id="text-input" placeholder="Enter text here">';
            break;

        case 'd': // Delete Line
            inputSection.innerHTML += '<input type="text" id="line-number-start" placeholder="Enter start line number (optional)">';
            inputSection.innerHTML += '<input type="text" id="line-number-end" placeholder="Enter end line number (optional)">';
            break;

        case 'l': // Load File
            inputSection.innerHTML += '<input type="file" id="file-input" accept=".txt">';
            break;

        case 'p': // Print Line
            inputSection.innerHTML += '<input type="text" id="print-line-start" placeholder="Enter start line number (optional)">';
            inputSection.innerHTML += '<input type="text" id="print-line-end" placeholder="Enter end line number (optional)">';
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

        case 'd': // Delete lines
            const startLineDel = parseInt(document.getElementById('line-number-start')?.value, 10);
            const endLineDel = parseInt(document.getElementById('line-number-end')?.value, 10);
            parameters = `${startLineDel} ${endLineDel}`;
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
            const startPrintLine = parseInt(document.getElementById('print-line-start')?.value, 10);
            const endPrintLine = parseInt(document.getElementById('print-line-end')?.value, 10);
            parameters = `${startPrintLine} ${endPrintLine}`;
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
    clearInputs(); // Clear input fields after processing command
}

function handleCommand(cmd, parameters) {
    const outputElement = document.getElementById('output');
    const args = parameters ? parameters.split(/\s+/) : [];

    switch (cmd) {
        case 'a': // Add text
            textFile.content += args.join(' ') + '\n';
            break;

        case 'd': // Delete lines
            const startLineDel = args.length > 0 ? parseInt(args[0], 10) - 1 : null;
            const endLineDel = args.length > 1 ? parseInt(args[1], 10) - 1 : null;

            if (startLineDel === null && endLineDel === null) {
                // Delete all lines
                textFile.content = '';
            } else if (startLineDel !== null && endLineDel === null) {
                // Delete specific line
                if (startLineDel >= 0 && startLineDel < textFile.content.split('\n').length) {
                    textFile.content = textFile.content.split('\n').filter((_, i) => i !== startLineDel).join('\n');
                } else {
                    alert("Line number out of bounds");
                }
            } else if (startLineDel !== null && endLineDel !== null) {
                // Delete range of lines
                if (startLineDel >= 0 && endLineDel >= startLineDel && endLineDel < textFile.content.split('\n').length) {
                    textFile.content = textFile.content.split('\n').filter((_, i) => i < startLineDel || i > endLineDel).join('\n');
                } else {
                    alert("Line range out of bounds");
                }
            } else {
                alert("Invalid line numbers");
            }
            break;

        case 'i': // Insert text
            const insertIndex = parseInt(args[0], 10) - 1;
            if (!isNaN(insertIndex)) {
                const lines = textFile.content.split('\n');
                lines.splice(insertIndex, 0, args.slice(1).join(' '));
                textFile.content = lines.join('\n');
            }
            break;

        case 'p': // Print lines
            const startPrintLine = args.length > 0 ? parseInt(args[0], 10) - 1 : null;
            const endPrintLine = args.length > 1 ? parseInt(args[1], 10) - 1 : null;

            console.log(startPrintLine, endPrintLine);
            const startNaN = isNan(startPrintLine);
            const lastNaN = isNaN(lastPrintLine);

            if (startPrintLine === null||startNaN && endPrintLine === null||lastNaN) {
                // Print all lines
                textFile.content.split('\n').forEach((line, index) => {
                    outputElement.innerHTML += `Line ${index + 1}: ${line}<br>`;
                });
            } else if (startPrintLine !== null||startNaN && endPrintLine === null||lastNaN) {
                // Print specific line
                if (startPrintLine >= 0 && startPrintLine < textFile.content.split('\n').length) {
                    const lines = textFile.content.split('\n');
                    outputElement.innerHTML += `Line ${startPrintLine + 1}: ${lines[startPrintLine]}<br>`;
                } else {
                    alert("Line number out of bounds");
                }
            } else if (startPrintLine !== null||startNaN && endPrintLine !== null||lastNaN) {
                // Print range of lines
                if (  (startPrintLine >= 0 && endPrintLine >= startPrintLine) && endPrintLine < textFile.content.split('\n').length) {
                    const lines = textFile.content.split('\n');
                    for (let i = startPrintLine; i <= endPrintLine; i++) {
                        outputElement.innerHTML += `Line ${i + 1}: ${lines[i]}<br>`;
                    }
                } else {
                    alert("Line range out of bounds");
                }
            } else {
                alert("Invalid line numbers");
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

function clearInputs() {
    document.querySelectorAll('#input-section input').forEach(input => input.value = '');
}

function quit() {
    // Reset text file content
    textFile.content = "";
    
    // Clear the output area
    document.getElementById('output').innerHTML = '';
    
    // Clear user inputs
    clearInputs();

    // Deselect any currently selected command
    document.querySelectorAll('.button-container button').forEach(button => {
        button.classList.remove('selected');
    });

    // Optionally, reset the filename if needed
    textFile.filename = "new.txt";

    alert("Everything has been reset. You can start again.");
}


