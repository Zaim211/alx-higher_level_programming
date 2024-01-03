#!/usr/bin/node
const request = require('request');
url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, request, body) {
  console.log(error || JSON.parse(body).title);
});
