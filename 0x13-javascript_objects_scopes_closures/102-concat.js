#!/usr/bin/node
const argum = process.argv.slice(2);
const fs = require('fs');
const fileOne = fs.readFileSync('./' + argum[0]);
const fileTwo = fs.readFileSync('./' + argum[1]);
fs.writeFileSync('./' + argum[2], fileOne + fileTwo);
