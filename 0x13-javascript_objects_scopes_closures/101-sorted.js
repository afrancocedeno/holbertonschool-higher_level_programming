#!/usr/bin/node
// import dict
const dict = require('./101-data').dict;

// new dict to concatenate
const newDict = {};

// iterate each key in the dict using 'in'
for (const key in dict) {
  if (newDict[dict[key]] === undefined) { newDict[dict[key]] = []; }

  // conmbine the keys in the new dict
  newDict[dict[key]].push(key);
}
console.log(newDict);
