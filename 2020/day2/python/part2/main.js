const regexgen = require('regexgen');
const fs = require('fs');

fs.readFile('./data.txt', 'utf-8', (err, data) => {
    if(err) {
        console.error(err);
        return;
    }
    console.log(regexgen(data.split("\n")))
})

// console.log(regexgen(['foobaz', 'foobaz', 'foozap', 'fooza']))