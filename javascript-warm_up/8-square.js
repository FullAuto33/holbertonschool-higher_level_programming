#!/usr/bin/node

const taille = Number(process.argv[2]);

if (isNaN(taille)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < taille; i++) {
    console.log('X'.repeat(taille));
  }
}
