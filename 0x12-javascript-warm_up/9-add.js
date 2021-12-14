#!/usr/bin/node
function add (a, b) {
  return a + b;
}
let sum = 0;
if (process.argv[2] && process.argv[3]) {
  sum = add(parseInt(process.argv[2]), parseInt(process.argv[3]));
  console.log(sum);
} else {
  console.log('NaN');
}
