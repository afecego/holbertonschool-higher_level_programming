#!/usr/bin/node
const list = [];
if (process.argv.length <= 3) {
  console.log(0);
} else {
  process.argv.forEach(function (arg) {
    const iter = parseInt(arg);
    if (!isNaN(iter)) {
      list.push(iter);
    }
  });
  list.sort(function (a, b) { return a - b; });
  list.pop();
  const result = list[list.length - 1];
  console.log(result);
}
