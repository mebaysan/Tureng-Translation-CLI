#! /bin/bash

# You should change `tureng-cli` with `python -m tureng_cli` to use by installing as a Python package;
# `pip install bs-tureng-cli` or `pip install git+https://github.com/BaysanSoft/Tureng-Translation-CLI.git`

N_RESULT=15

if [[ -n $3 ]]; then
	N_RESULT=$3
fi


if [[ $1 != "translate" && $1 != "sentence" && $1 != "synonym" ]]; then
	tureng-cli translate  -w "$1" -n $N_RESULT
else
	tureng-cli $1 -w "$2" -n $N_RESULT
fi
