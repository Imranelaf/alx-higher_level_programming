#!/usr/bin/node
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
req(url, function (error, res, body) {
  console.log(error || JSON.parse(body).title);
});
