#!/usr/bin/node

const one = Number(process.argv[2]);
const two = Number(process.argv[3]);

function add (one, two) {
  return one + two;
}

console.log(add(one, two));
