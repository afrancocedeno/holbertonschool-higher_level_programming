#!/usr/bin/node
/* prints the nomber of movies */
const request = require('request');
const characterID = 18;
const url = process.argv[2];

request.get(url, (error, _response, body) => {
  /* error edge case */
  if (error) { return (console.log(error)); }

  /* movie data to traverse */
  const moviesData = JSON.parse(body).results;

  /* a variable match counter */
  let matchCounter = 0;

  /* an array for each movie */
  moviesData.forEach(movie => {
    /* an array for each character */
    movie.characters.forEach(character => {
      /* if match the char, increment */
      if (character.includes(characterID)) { matchCounter++; }
    });
  });
  console.log(matchCounter);
});
