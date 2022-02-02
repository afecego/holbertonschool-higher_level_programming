#!/usr/bin/node
const request = require('request');
const web = process.argv[2];
const dicNew = {};

request(web, (err, res, body) => {
  if (err) {
    console.error(err);
  }
  const json = JSON.parse(body);

  for (const row of json) {
    const id = row.userId;
    if (row.completed) {
      if (dicNew[id] === undefined) {
        dicNew[id] = 1;
      } else {
        dicNew[id] += 1;
      }
    }
  }
  console.log(dicNew);
});
