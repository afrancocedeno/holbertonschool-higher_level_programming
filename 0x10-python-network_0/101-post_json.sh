#!/bin/bash
# post a json file using curl
curl $1 -X POST -H "Content-Type: application/json" -d @$2
