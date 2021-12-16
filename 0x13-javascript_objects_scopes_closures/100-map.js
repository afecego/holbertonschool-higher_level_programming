#!/usr/bin/node
const newList = require('./100-data.js').list;
console.log(newList);
let iter = 0;
const map1 = newList.map(x => x * iter++);
console.log(map1);
