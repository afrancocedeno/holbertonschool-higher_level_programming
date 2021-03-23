#!/usr/bin/node
const myVar = 'C is fun';
const printQuantity = parseInt(process.argv[2]);
let i = 0;
while (i < printQuantity) { console.log(myVar); i++; }
