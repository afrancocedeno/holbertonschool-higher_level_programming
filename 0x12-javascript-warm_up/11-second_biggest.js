#!/usr/bin/node
const myArgs = process.argv.slice(2);
let i = 1;
// sort in reverse
myArgs.sort().reverse();
// edge cases
if (process.argv.length === 2 || process.argv.length === 3) console.log(0);
for (; i < process.argv.length; i++) {
  if (myArgs[i + 1] !== myArgs[i]) {
    console.log(myArgs[i + 1]);
    break;
  }
}
