#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.heigth = h;
    }
  }

  print () {
    const myVar = 'X';
    let i = 0;
    // if (isNaN(h or w)) console.log('Missing size');
    while (i < this.heigth) { console.log(myVar.repeat(this.width)); i++; }
  }
}
module.exports = Rectangle;
