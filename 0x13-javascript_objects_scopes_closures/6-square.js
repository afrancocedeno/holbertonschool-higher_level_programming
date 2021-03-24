#!/usr/bon/node
const copySquare = require('./5-square');
// use a differente name inheritance
module.exports = class Square extends copySquare {
  // create the instance method
  charPrint(c) {
    // if c is undefined use char X
    if (c === undefined) { this.print(); }
    else { for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }}
  }
}
