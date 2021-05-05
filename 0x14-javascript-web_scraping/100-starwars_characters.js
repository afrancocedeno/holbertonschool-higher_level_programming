#!/usr/bin/node

/* script that prints all the characters of a movie ID */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const movieID = process.argv[2];

request.get(url + movieID + '/', (error, _response, body) => {
  if (error) { console.log(error); }

  /* retrieve the path for each movie match */
  const moviePaths = JSON.parse(body).characters;

  for (let element in moviePaths) {
    request.get(moviePaths[element], (error, _response, body) => {
      if (error) { console.log(error); }
      movieName = JSON.parse(body).name;
      console.log(movieName);
    });
  };
});
