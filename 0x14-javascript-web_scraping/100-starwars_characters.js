#!/usr/bin/node
const request = require('request');
const web = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
const webNew = web + id;

request(webNew, (err, res, body) => {
  if (err) {
    console.error(err);
  }
  const json = JSON.parse(body).characters;
  for (let i = 0; i < json.length; i++) {
    request(json[i], (err, res, body) => {
      if (err) {
        console.error(err);
      }
      const char = JSON.parse(body).name;
      console.log(char);
    });
  }
});
