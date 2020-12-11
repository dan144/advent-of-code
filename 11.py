#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

FLOOR = '.'
EMPTY = 'L'
OCCPD = '#'

seats = {}
y = 0
with open(input_file) as f:
    for line in f:
        for x in range(len(line[:-1])):
            seats[y, x] = line[x]
        y += 1

def run(og_seats, occ_adj, find_first):
    seats = og_seats.copy()
    change = True
    while change:
        change = False
        ns = {}
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
                        if not find_first or seats[ny, nx] != FLOOR:
                            found = True

                        if seats[ny, nx] == OCCPD:
                            if seats[y, x] == EMPTY:
                                adj += 1
                            if seats[y, x] == OCCPD:
                                adj += 1
    
            if seats[y, x] == EMPTY and adj == 0:
                ns[y, x] = OCCPD
                change = True
            elif seats[y, x] == OCCPD and adj >= occ_adj:
                ns[y, x] = EMPTY
                change = True
            else:
                ns[y, x] = seats[y, x]
        seats = ns
    return list(seats.values()).count(OCCPD)

p1 = run(seats, 4, False)
print(f'Part 1: {p1}')

p2 = run(seats, 5, True)
print(f'Part 2: {p2}')
