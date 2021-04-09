#!/bin/bash
# post a json file using curl
curl -s $1 -X POST -H "Content-Type: application/json" -d @$2
