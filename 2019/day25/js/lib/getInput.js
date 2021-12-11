let fs = require('fs');
let path = require('path');
let http = require('https');
let readline = require('readline');

function getInput(year, day) {
    return new Promise((resolve, reject) => {
        let rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout,
            terminal: false
        });

        let data = '';
        let timeout;

        function handleData(line) {
            clearTimeout(timeout);
            data += line + '\n';
        }

        function handleEnd() {
            resolve(data.replace(/\n$/, ''));
        }

        rl.on('line', handleData);
        rl.on('close', handleEnd);

        timeout = setTimeout(() => {
            rl.removeAllListeners();
            process.stdin.pause();
            getFile(year, day, resolve, reject);
        }, 100);
    });
}

function getFile(year, day, resolve, reject) {
    let currentDirectory = path.dirname(require.main.filename);
    let inputFileName = path.resolve(currentDirectory, 'input.txt');
    fs.exists(inputFileName, (exists) => {
        if(exists) {
            fs.readFile(inputFileName, 'utf-8', (err, data) => {
                if(err) {
                    return reject(err);
                }
                resolve(data.replace(/\r\n/g, '\n').replace(/\n$/, ''));
            });
        }
        else {
            // Auth cookie should be in a file named auth_cookie.txt in the same directory as this lib file.
            // Don't commit to source!!
            fs.readFile(path.resolve(__dirname, 'auth_cookie.txt'), 'utf-8', (err, secret) => {
                if(err) {
                    return reject(err);
                }
                let fileStream = fs.createWriteStream(inputFileName);
                let options = {
                    protocol: 'https:',
                    hostname: 'adventofcode.com',
                    path: `/${year}/day/${day}/input`,
                    headers: {'Cookie': 'session=' + secret}
                }
                let request = http.get(options, (response) => {
                    if(response.statusCode !== 200) {
                        fs.unlink(inputFileName, () => { });
                        reject(`Could not download from ${options.protocol}\/\/${options.hostname}${options.path} - ${response.statusCode} ${response.statusMessage}`)
                    }
                    else {
                        response.pipe(fileStream);
                        fileStream.on('finish', () => {
                            fileStream.close(() => {
                                fs.readFile(inputFileName, 'utf-8', (err, data) => {
                                    if(err) {
                                        return reject(err);
                                    }
                                    resolve(data.trim());
                                });
                            });
                        });
                    }
                }).on('error', (err) => {
                    fs.unlink(inputFileName);
                    reject(err.message);
                });
            });
        }
    });
}

module.exports = getInput;
