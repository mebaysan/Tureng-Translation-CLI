#! /bin/bash

SEARCH_TERM=$1

python3 -m tureng_cli translate -w "$SEARCH_TERM" -n 15
