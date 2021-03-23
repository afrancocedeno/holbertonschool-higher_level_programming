#!/usr/bin/node
const myArgs = process.argv.slice(2);
let i = 0;
myArgs.sort().reverse();
if (process.argv.length <= 3) console.log(0);
else if (myArgs[i + 1] === myArgs[i]) console.log(myArgs[i]);
else {
  for (; i < process.argv.length; i++) {
    if (myArgs[i + 1] < myArgs[i]) {
      console.log(myArgs[i + 1]);
      break;
    }
  }
}
