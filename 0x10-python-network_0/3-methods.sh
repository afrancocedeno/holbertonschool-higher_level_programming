#!/bin/bash
# comment comment
sed 's/: /\n/g' <<< curl -sIL localhost:5000/route_4 | grep 'Allow'
