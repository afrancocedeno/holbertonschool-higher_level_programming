#!/usr/bin/node
const factorialSize = parseInt(process.argv[2]);
function factorial (number) {
  if (isNaN(number)) return (1);
  if (number === 0) return (1);
  return (number * factorial(number - 1));
}
console.log(factorial(factorialSize));
