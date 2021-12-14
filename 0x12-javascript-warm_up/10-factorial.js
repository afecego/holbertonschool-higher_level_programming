#!/usr/bin/node
function factorial (x) {
  if (x > 0) {
    return (x * factorial(x - 1));
  } else {
    return 1;
  }
}
const x = process.argv[2];
const answer = factorial(x);
console.log(answer);
