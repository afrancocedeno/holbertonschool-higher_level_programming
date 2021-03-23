#!/usr/bin/node
const myArgs = process.argv.slice(2);
let i = 0;

// sort in reverse
myArgs.sort(function(a, b) { return (b - a); });

// Edge cases
if (process.argv.length <= 3) console.log(0);

// if more than one argument
else {
  for (; i < process.argv.length; i++) {
    // if end of the list
    if (isNaN(myArgs[i + 1])) { console.log(myArgs[i + 1]); break; }
    if (myArgs[i + 1] < myArgs[i]) {
      console.log(myArgs[i + 1]);
      break;
    }
  }
}
