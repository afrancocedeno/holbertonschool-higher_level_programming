#!/usr/bin/node
const fs = require('fs');
// catch arguments and read the files
const data1 = fs.readFileSync(process.argv[2], 'utf8');
const data2 = fs.readFileSync(process.argv[3], 'utf8');
// concatenate them
const dataJoin = data1 + data2;
// write data into file last argumernt
fs.writeFileSync(process.argv[4], dataJoin, 'utf8');
