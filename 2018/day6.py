#!/usr/bin/python3

import json
import sys

import utils

print('Running:',sys.argv[0])

testing = len(sys.argv) == 2

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)

if testing:
    print('TESTING')
    input_file = 'test' + input_file

print('Reading:', input_file)

inputs = []
max_man_sum = 10000
data_type = str
with open(input_file, 'r') as f:
    if testing:
        test_vals = json.loads(f.readline())
        max_man_sum = test_vals['max_man_sum']
        part_one = test_vals['part_one']
        part_two = test_vals['part_two']
    for line in f:
        inputs.append(data_type(line[:-1]))
if testing:
    print(inputs)

print()
print('PART ONE')

coords = []
min_x = None
max_x = None
min_y = None
max_y = None
for n in range(len(inputs)):
    line = inputs[n]
    x, y = line.split(', ')
    x = int(x)
    y = int(y)
    if not min_x or x < min_x:
        min_x = x
    if not max_x or x > max_x:
        max_x = x
    if not min_y or y < min_y:
        min_y = y
    if not max_y or y > max_y:
        max_y = y
    coords.append([x, y, n, 0])

on_edge = set()
safe_region = 0
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        min_d = None
        val = None
        min_count = 0
        dist_from = 0
        for n in range(len(coords)):
            coord = coords[n]
            man_d = utils.manh(coord[:2], (x, y))
            if min_d is None or man_d < min_d:
                min_d = man_d
                val = n
                min_count = 1
            elif man_d == min_d:
                min_count += 1
            dist_from += man_d
        if min_count == 1:
            if x in (min_x, max_x) or y in (min_y, max_y):
                on_edge.add(val)
            coords[val][3] += 1
        safe_region += 1 if dist_from < max_man_sum else 0

r_coords = [x for x in sorted(coords, key=lambda x: x[3]) if x[2] not in on_edge]
print('Largest region:', r_coords[-1][3])
if testing:
    if r_coords[-1][3] == part_one:
        print('PART ONE CORRECT')
    else:
        print('PAT ONE FAILED')

print()
print('PART TWO')
print('Safe regions:', safe_region)
if testing:
    if safe_region == part_two:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')

# safe_region = sum([sum([1 if sum((abs(coord[0] - x) + abs(coord[1] - y)) for coord in coords) < max_man_sum else 0 for y in range(min_y, max_y + 1)]) for x in range(min_x, max_x + 1)])
