#!/usr/bin/node

const request = require('request');

/* script that computes the number of tasks completed by user id */

const url = process.argv[2];

request.get(url, (error, _response, body) => {
  if (error) { return (console.log(error)); }

  /* retrieve userid, id and title from url */
  const content = JSON.parse(body);

  const resultDic = {};
  let userIDKey;
  let completedKey;

  for (const element in content) {
    /* retrive the userid key content in each element */
    userIDKey = content[element].userId;

    /* retrive the complete key content in each element */
    completedKey = content[element].completed;

    /* if completed key is not null increment */
    if (completedKey) {
      /* if value is null do not incremet */
      if (!resultDic[userIDKey]) { resultDic[userIDKey] = 0; }

      /* other wise increment */
      resultDic[userIDKey]++;
    }
  }
  console.log(resultDic);
});
