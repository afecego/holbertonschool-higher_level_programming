#!/usr/bin/node
const request = require('request');
const web = process.argv[2];

request
  .get(web)
  .on('response', function (response) {
    console.log('code: ' + response.statusCode); // 200
  });
