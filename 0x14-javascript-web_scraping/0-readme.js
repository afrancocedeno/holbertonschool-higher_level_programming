#!/usr/bin/node

/* fs: file system node module. Allow code to interact with files */
const fs = require('fs');

/* process.argv[2] <-- arguments with node js */
const file = process.argv[2];

const encoding = 'utf8';

fs.readFile(file, encoding, function (err, fileContent) {
  /* if error message is prompted return it */
  if (err) { return console.error(err); }

  /* otherwise print the data */
  console.log(fileContent);
});
