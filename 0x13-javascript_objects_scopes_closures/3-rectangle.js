#!/usr/bin/node
/* a class Rectangle that defines a rectangle
 * Create an instance method called print()
 * that prints the rectangle using the character X
 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.height = h;
      this.width = w;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
