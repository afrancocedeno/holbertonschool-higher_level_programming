#!/bin/bash
# retrieves the status code of the response by a given request from URL arg
curl -sI $1 -w "%{http_code}" -o /dev/null
