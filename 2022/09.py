#!/usr/bin/env python3

import sys

import utils
### available functions:
# display_grid((y, x) grid) - display values in 2D map grid
# transpose_grid(grid) - swap key values from (x, y) to (y, x) and back

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.strip())

def run(n_tails):
    head = [0, 0]
    tails = []
    for _ in range(n_tails):
        tails.append([0, 0])
    tail_pos = {(0, 0)}
    for line in inp:
        d, dist = line.split()
        dist = int(dist)
        for step in range(dist):
            # move head
            if d == 'R':
                head[0] += 1
            elif d == 'L':
                head[0] -= 1
            elif d == 'U':
                head[1] += 1
            elif d == 'D':
                head[1] -= 1
            else:
                assert False
    
            # move tail(s)?
            for i, tail in enumerate(tails):
                following = head if i == 0 else tails[i - 1]
                dx = tail[0] - following[0]
                dy = tail[1] - following[1]
                if abs(dx) > 1 or abs(dy) > 1:
                    if dx != 0:
                        tail[0] += 1 if (dx < 0) else -1
                    if dy != 0:
                        tail[1] += 1 if (dy < 0) else -1
    
            tail_pos.add(tuple(tails[-1]))
    
            #grid = {}
            #for pos in tail_pos:
            #    grid[pos] = '#'
            #grid[tuple(head)] = 'H'
            #grid[tuple(tails[-1])] = 'T'
            #grid = utils.transpose_grid(grid)
            #utils.display_grid(grid)
            #input()
    return len(tail_pos)

p1 = run(1)
print(f'Part 1: {p1}')
p2 = run(9)
print(f'Part 2: {p2}')
