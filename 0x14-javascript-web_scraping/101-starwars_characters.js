#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieID = process.argv[2];

const data = {};

request.get(url + movieID + '/', (error, _response, body) => {
  if (error) { return (console.log(error)); }

  const moviePaths = JSON.parse(body).characters;

  for (const element in moviePaths) {
    request.get(moviePaths[element], (error, _response, body) => {
      if (error) return console.log(error);

      data[element] = JSON.parse(body).name;
    });
  }
});

/* time out setting */
setTimeout(() => print(data), 10000);

/* traverse and print */
function print (content) {
  for (const element in content) {
    console.log(content[element]);
  }
}
