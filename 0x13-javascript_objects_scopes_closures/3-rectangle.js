#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.heigth = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.heigth) { console.log('X'.repeat(this.width)); i++; }
  }
}

module.exports = Rectangle;
