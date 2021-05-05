#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];

/* url Star wars API */
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + movieID, (error, response, body) => {
  if (error) { return console.log('error:', error); }
  console.log(JSON.parse(body).title);
});
