#!/usr/bin/node
const request = require('request');
const web = process.argv[2];
let count = 0;

request(web, (err, res, body) => {
  if (err) {
    console.error(err);
  }

  const json = JSON.parse(body).results;

  for (let i = 0; i < json.length; i++) {
    const charac = json[i].characters;

    for (let j = 0; j < charac.length; j++) {
      const chara = charac[j];
      if (chara === 'https://swapi-api.hbtn.io/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
});
