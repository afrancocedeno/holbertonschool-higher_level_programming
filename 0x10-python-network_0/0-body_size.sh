#!/bin/bash
# script sends a request, and displays the size of the body of the response
curl -sI localhost:5000 | grep "Content-Length" | cut -d ' ' -f 2
