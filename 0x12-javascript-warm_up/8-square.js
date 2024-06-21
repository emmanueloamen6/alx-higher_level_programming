#!/usr/bin/node
/* a script that prints a square.
 * The first argument is the size of the square.
 * If the first argument can’t be converted to an integer,
 * print “Missing size”.
 * You must use the character X to print the square.
 */
const size = process.argv[2];

if (size === undefined || isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  for (let j = 0; j < parseInt(size); j++) {
    let row = '';
    for (let i = 0; i < parseInt(size); i++) {
      row += 'X';
    }
    console.log(row);
  }
}
