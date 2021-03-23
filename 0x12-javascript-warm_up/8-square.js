#!/usr/bin/node
const myVar = 'X';
const printQuantity = parseInt(process.argv[2]);
let i = 0;
if (isNaN(printQuantity)) console.log('Missing size');
while (i < printQuantity) { console.log(myVar.repeat(printQuantity)); i++; }
