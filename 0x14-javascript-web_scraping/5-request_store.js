#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const [url, fileContent] = process.argv.slice(2, 4);
const encoding = 'utf8';

/* request try */
request.get(url, (error, _response, body) => {
  if (error) { console.log(error); }

  /* write in file try */
  fs.writeFile(fileContent, body, encoding, error => {
    /* if fail error handling */
    if (error) { console.log(error); }
  });
});
