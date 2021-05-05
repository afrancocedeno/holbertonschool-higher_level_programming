#!/usr/bin/node

/* fs: file system node module. Allow code to interact with files */
const fs = require('fs');

/* process.argv[2] <-- arguments with node js */
const file = process.argv[2];

const encoding = 'utf8';

fs.readFile(file, encoding, (err, fileContent) => {
  /* if error is not null message is prompted return it */
  if (err) { return console.log(err); }

  /* otherwise print the data */
  console.log(fileContent);
});
