#!/usr/bin/node
if (process.argv[2]) {
  if (isNaN(process.argv[2])) {
    console.log('Not a number');
  } else {
    console.log((process.argv[2]));
  }
} else {
  console.log('Not a number');
}
