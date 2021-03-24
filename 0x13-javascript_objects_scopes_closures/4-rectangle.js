#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
		  this.width = w;
		  this.height = h;
    }
  }

  // instance method to print the rectangle
  print () {
    for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }

  // instance method to rotate the rectangle
  rotate () {
    this.width = this.height;
    this.height = this.width;
  }

  // instance method to duplicate the rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
