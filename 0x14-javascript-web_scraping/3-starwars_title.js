#!/usr/bin/node
const request = require('request');
const web = 'https://swapi-api.hbtn.io/api/films/';
const webId = process.argv[2];
const api = web + webId;

request(api, (err, res, body) => {
  if (err) {
    console.error(err);
  }
  const json = JSON.parse(body);
  const title = json.title;
  console.log(title);
});
