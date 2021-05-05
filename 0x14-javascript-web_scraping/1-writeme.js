#!/usr/bin/node

/* fs: file system node module. Allow code to interact with files */
const fs = require('fs');

/* process.argv[2] <-- arguments with node js */
const filePath = process.argv[2];

/* content to add as an arg */
const fileContent = process.argv[3];

const encoding = 'utf8';

fs.write(filePath, fileContent, encoding, (err) => {
  /* if error is not null message is prompted return it */
  if (err) { return console.log(err); }
});
