#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    inp = utils.load_split_lines(f) # asdf asdf asdf ...

def make_grid(diags):
    grid = {}
    for line in inp:
        x1, y1 = map(int, line[0].split(','))
        x2, y2 = map(int, line[2].split(','))
        if x1 == x2:
            ymn, ymx = sorted([y1, y2])
            for y in range(ymn, ymx+1):
                v = grid.get((x1, y), 0)
                grid[x1, y] = v + 1
        elif y1 == y2:
            xmn, xmx = sorted([x1, x2])
            for x in range(xmn, xmx+1):
                v = grid.get((x, y1), 0)
                grid[x, y1] = v + 1
        elif diags: # only for Part 2, so toggle
            xmn, xmx = sorted([x1, x2])
            ymn, ymx = sorted([y1, y2])
            d = xmx - xmn # how far to go

            # determine which direction to go, down/right or down/left
            mul = 1 if (y1 > y2) == (x1 > x2) else -1

            # alternative: could determine which end to start at based on mul
            #ystart, yend = sorted([y1, y2], reverse=(mul == -1))

            for i in range(d+1):
                x = xmn + i
                y = ymn + i if mul == 1 else ymx - i
                # alternative: go from start and step by sign of mul
                #y = ystart + i * mul
                v = grid.get((x, y), 0)
                grid[x, y] = v + 1

    total = 0
    for v in grid.values():
        if v > 1:
            total += 1
    return total

p1 = make_grid(False)
print(f'Part 1: {p1}')

p2 = make_grid(True)
print(f'Part 2: {p2}')
