#!/usr/bin/node
// import list from 100-data
const list = require('./100-data').list;

// arroy function to multiply index
const indexProduct = (value, index) => value * index;

const newList = list.map(indexProduct);

// print lists
console.log(list);
console.log(newList);
