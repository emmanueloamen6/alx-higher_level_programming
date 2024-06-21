#!/usr/bin/node
/* script that prints the addition of 2 integers
 * The first argument is the first integer
 * The second argument is the second integer
 * function with this prototype: function add(a, b)
 */
const first = process.argv[2];
const second = process.argv[3];

function add(a, b) {
  return a + b;
}

const a = parseInt(first);
const b = parseInt(second);

console.log(add(a, b));
