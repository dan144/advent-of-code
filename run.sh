#!/bin/bash

number=`date | cut -d' ' -f4`
./day$number.py
