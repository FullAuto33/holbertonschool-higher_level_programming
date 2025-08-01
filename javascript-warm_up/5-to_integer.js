#!/usr/bin/node
const input = process.argv[2];
const num = parseFloat(input);

if (isNaN(num)) {
    console.log('Not a number');
}
else {
    const intNum = Math.floor(num);
    console.log('My number: ' + intNum);
}
