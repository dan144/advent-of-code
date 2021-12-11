#!/usr/bin/env python3

from copy import copy

import sys

import utils
### available functions:
# display_grid
# adjs - set of dx,dy values for LRUD adjacencies
# diags - set of dx,dy values for diagonals
# all_dirs set of dx,dy values for all 8 surrounding values

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    inp = utils.load_grid(f, int) # 2D grid of X type

# Part 1
def step(inp):
    n_flash = 0
    flashes = set()
    for (x, y), energy in copy(inp).items():
        inp[x, y] += 1
        if inp[x, y] > 9:
            flashes.add((x, y))

    done = set()
    while flashes:
        new = set()
        for x, y in flashes:
            for dx, dy in utils.all_dirs:
                nx = x + dx
                ny = y + dy
                if (nx, ny) in inp:
                    inp[nx, ny] += 1
                    if inp[nx, ny] > 9 and (nx, ny) not in done | flashes:
                        new.add((nx, ny))
        done.update(flashes)
        flashes = new
        
    for (x, y), energy in copy(inp).items():
        if energy > 9:
            n_flash += 1
            inp[x, y] = 0
    return n_flash

for _ in range(100):
    p1 += step(inp)
print(f'Part 1: {p1}')

# Part 2
p2 = 100 # known from part 1; if converged earlier this will be wrong
while len(set(inp.values())) > 1:
    step(inp)
    p2 += 1
print(f'Part 2: {p2}')
