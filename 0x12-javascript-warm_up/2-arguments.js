#!/usr/bin/node
/*
if (condition) code to run if condition is true
else run some other code instead
*/
// store the length of arguments
const myVar = process.argv.length;
// compare different cases
if (myVar === 2) console.log('No argument');
else if (myVar === 3) console.log('Argument found');
else if (myVar > 3) console.log('Arguments found');
