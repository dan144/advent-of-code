#!/usr/bin/python3

import sys

print('Running:',sys.argv[0])

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)
print('Reading:', input_file)

inputs = []
data_type = str
with open(input_file, 'r') as f:
    for line in f:
        inputs.append(data_type(line[:-1]))

print()
print('PART ONE')

coords = []
min_x = None
max_x = None
min_y = None
max_y = None
#inputs = ['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9'] # test
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
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        min_d = None
        val = None
        min_count = 0
        for n in range(len(coords)):
            coord = coords[n]
            man_d = abs(coord[0] - x) + abs(coord[1] - y)
            if min_d is None or man_d < min_d:
                min_d = man_d
                val = n
                min_count = 1
            elif man_d == min_d:
                min_count += 1
        if min_count == 1:
            if x in (min_x, max_x) or y in (min_y, max_y):
                on_edge.add(val)
            coords[val][3] += 1

r_coords = [x for x in sorted(coords, key=lambda x: x[3]) if x[2] not in on_edge]
print('Largest region:', r_coords[-1][3])

print()
print('PART TWO')

# safe_region = sum([sum([1 if sum((abs(coord[0] - x) + abs(coord[1] - y)) for coord in coords) < 10000 else 0 for y in range(min_y, max_y + 1)]) for x in range(min_x, max_x + 1)])
safe_region = 0
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        safe_region += 1 if sum((abs(coord[0] - x) + abs(coord[1] - y)) for coord in coords) < 10000 else 0
print('Safe regions:', safe_region)
