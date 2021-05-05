#!/usr/bin/node
/* status code of a get request */
/* request:  http request module. */
const request = require('request');

const url = process.argv[2];

request.get(url).on('response', (response) => {
  /* output: "code: <status code>" */
  console.log('code:', response.statusCode);
});
