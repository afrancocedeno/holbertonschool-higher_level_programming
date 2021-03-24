#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
// define an counter for each occurence
  let ocurrencesCounter = 0;
  // traverse the list
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) { ocurrencesCounter++; }
  }
  // return number of occurences
  return (ocurrencesCounter);
};
