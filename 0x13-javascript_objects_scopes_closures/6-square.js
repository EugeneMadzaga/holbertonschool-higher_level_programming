#!/usr/bin/node
const SquareA = require('./4-rectangle.js');
module.exports = class Square extends SquareA {
  charPrint (c) {
    if (c === undefined) {
      return this.print(x);
    } else {
      let A = '';
      for (let i = 0; i < this.width; i++) {
        A += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(A);
      }
    }
  }
};
