#!/usr/bin/node
function callMeMoby (x, theFunction) {
	let i = 0;
	for (; i < x; i++) { theFunction(); };
      }
module.exports.callMeMoby = callMeMoby;
