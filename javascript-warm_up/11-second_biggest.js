#!/usr/bin/node

const argument = process.argv.slice(2).map(Number);

if (argument.length < 2) {
  console.log(0);
} else {
  let maximum = Number.MIN_SAFE_INTEGER;
  let twomax = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < argument.length; i++) {
    if (argument[i] > max) {
      twomax = max;
      max = argument[i];
    } else if (argument[i] > twomax && argument[i] < max) {
      twomax = argument[i];
    }
  }

  console.log(twomax);
}
