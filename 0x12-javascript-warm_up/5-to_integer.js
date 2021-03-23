#!/usr/bin/node
// parseInt: converts a strings to an integer
const myVar = parseInt(process.argv[2]);
if (isNaN(myVar)) console.log('Not a number');
else console.log(`My number: ${myVar}`);
