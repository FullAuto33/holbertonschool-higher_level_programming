#!/usr/bin/node
const num = parseInt(process.argv[2]);
const num = parseFloat(input);
const intNum = Math.floor(num);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + intNum);
}
