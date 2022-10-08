#! /bin/bash

N_RESULT=15

if [[ -n $3 ]]; then
	N_RESULT=$3
fi


if [[ $1 != "translate" && $1 != "sentence" && $1 != "synonym" ]]; then
	python3 -m tureng_cli translate  -w "$1" -n $N_RESULT
else
	python3 -m tureng_cli $1 -w "$2" -n $N_RESULT
fi
