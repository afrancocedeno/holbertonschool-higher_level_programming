#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sIL 0.0.0.0:5000/route_4 | grep 'Allow' | sed 's/Allow: //g'
