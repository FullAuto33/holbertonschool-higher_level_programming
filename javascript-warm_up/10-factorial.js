#!/usr/bin/node

const number = parseInt(process.argv[2]);

function factorial (x) {
  if (isNaN(x) || x < 0) {
    return 1;
  }
  if (x === 0) {
    return 1;
  }
  return x * factorial(x - 1);
}

console.log(factorial(number));
