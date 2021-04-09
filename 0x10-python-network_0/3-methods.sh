#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sIL $1 | grep 'Allow' | sed 's/Allow: //g'
