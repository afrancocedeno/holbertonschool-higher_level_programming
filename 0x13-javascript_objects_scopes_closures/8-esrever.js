#!/usr/bin/node
exports.esrever = function (list) {
  // traverse until the middle of the list
  for (let i = 0; i < (list.length / 2); i++) {
    // exchange each value in the list
    [list[i], list[list.length - 1 - i]] = [list[list.length - 1 - i], list[i]];
  }
  // return the list reversed
  return (list);
};
