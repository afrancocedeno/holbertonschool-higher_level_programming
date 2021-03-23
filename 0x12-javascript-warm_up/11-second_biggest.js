#!/usr/bin/node
const myArgs = process.argv.slice(2);
let i = 0;
// sort in reverse
myArgs.sort().reverse();
// edge cases
if (process.argv.length === 2 || process.argv.length === 3) console.log(0);
else {
  for (; i < process.argv.length; i++) {
    if (myArgs[i] !== myArgs[i - 1]) {
      console.log(myArgs[i]);
      break;
    }
  }
}
