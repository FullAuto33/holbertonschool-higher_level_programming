#!/usr/bin/node
const nombre = Number(process.argv[2]);

if (isNaN(nombre)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < nombre; i++) {
    console.log('C is fun');
  }
}
