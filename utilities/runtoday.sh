#!/bin/bash

if [ -z "$1" ]; then
  number=`date | cut -d' ' -f3`
else
  number=$1
fi

echo "Test run"
./day$number.py -t
echo
echo
echo "Running"
time ./day$number.py
