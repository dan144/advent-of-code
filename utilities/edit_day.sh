#!/bin/bash

set -eu

YEAR=$1
DAY=$(printf "%02d" $2)

if [ $YEAR -lt 2015 ] || [ $YEAR -gt 2020 ]; then
    echo "Year $YEAR not valid"
    exit 1
fi

if [ $DAY -lt 1 ] || [ $DAY -gt 25 ]; then
    echo "Day $DAY not valid"
    exit 1
fi

[ $(basename $(pwd)) == "utilities" ] && cd ..

if [ ! -d $YEAR ]; then
    mkdir -p $YEAR
fi

if ls $YEAR/$DAY*; then
    FILENAME="$YEAR/$DAY*"
else
    FILENAME="$YEAR/$DAY.py"
    if [ ! -f $YEAR/$DAY.py ]; then
        cp utilities/framework.py $FILENAME
    fi
fi

vim -p $FILENAME $YEAR/input$DAY $YEAR/input$DAY.test
