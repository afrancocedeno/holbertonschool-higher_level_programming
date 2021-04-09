#!/bin/bash
# script that post srguments
curl -s $1 -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST
