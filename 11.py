#!/usr/bin/env python3

import re
import sys

from copy import deepcopy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

seats = {}
y = 0
with open(input_file) as f:
    for line in f:
        for x in range(len(line[:-1])):
            seats[y, x] = line[x]
        y += 1
os = deepcopy(seats)

mx = x
change = True
while change:
    change = False
    ns = {}
    occ = 0
    for y, x in seats.keys():
        adj = 0
        for dy in {-1, 0, 1}:
            for dx in {-1, 0, 1}:
                if dy == 0 and dx == 0:
                    continue
                ny = y + dy
                nx = x + dx
                if (ny, nx) not in seats.keys():
                    continue
                if seats[y, x] == 'L':
                    if seats[ny, nx] == '#':
                        adj += 1
                if seats[y, x] == '#':
                    if seats[ny, nx] == '#':
                        adj += 1

        if seats[y, x] == 'L' and adj == 0:
            ns[y, x] = '#'
        elif seats[y, x] == '#' and adj >= 4:
            ns[y, x] = 'L'
        else:
            ns[y, x] = seats[y, x]
        occ += ns[y, x] == '#'
        change = change or (seats[y, x] != ns[y, x])
    seats = ns

p1 = occ
print(f'Part 1: {p1}')

seats = os
change = True
while change:
    change = False
    ns = {}
    occ = 0
    for y, x in seats.keys():
        adj = 0
        for dy in {-1, 0, 1}:
            for dx in {-1, 0, 1}:
                if dy == 0 and dx == 0:
                    continue
                found = False
                ny, nx = y, x
                while not found:
                    ny = ny + dy
                    nx = nx + dx
                    if (ny, nx) not in seats.keys():
                        found = True # off board
                        continue
                    if seats[ny, nx] != '.':
                        found = True
                    if seats[y, x] == 'L':
                        if seats[ny, nx] == '#':
                            adj += 1
                    if seats[y, x] == '#':
                        if seats[ny, nx] == '#':
                            adj += 1

        if seats[y, x] == 'L' and adj == 0:
            ns[y, x] = '#'
        elif seats[y, x] == '#' and adj >= 5:
            ns[y, x] = 'L'
        else:
            ns[y, x] = seats[y, x]
        occ += ns[y, x] == '#'
        change = change or (seats[y, x] != ns[y, x])
        # print(seats[y, x], adj, ns[y, x])
    seats = ns

p2 = occ
print(f'Part 2: {p2}')
