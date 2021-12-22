#!/usr/bin/env python3

import re
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        cmd = line.strip().split()[0]
        inp.append([cmd] + list(map(int, re.findall(r'-?[0-9]+', line))))

# Part 1
# original part 1 solution; could be replaced by adapted part 2 solution
def run(lim):
    grid = {}
    for line in inp:
        cmd = line[0]
        for x in range(max(line[1], -lim), min(line[2], lim) + 1):
            for y in range(max(line[3], -lim), min(line[4], lim) + 1):
                for z in range(max(line[5], -lim), min(line[6], lim) + 1):
                    if cmd == 'on':
                        grid[x, y, z] = 1
                    else:
                        try:
                            grid.pop((x, y, z))
                        except KeyError:
                            pass
    return grid

p1 = sum(run(50).values())
print(f'\rPart 1: {p1}')

# Part 2
def vol(cube):
    x = cube[1] - cube[0] + 1
    y = cube[3] - cube[2] + 1
    z = cube[5] - cube[4] + 1
    return x*y*z

def scoop(c1, c2):
    # this fxn returns all sub-cubes of c1 that do not overlap with c2
    frags = []

    # check for no intersection
    for i in (0, 2, 4):
        if c2[i] > c1[i+1] or c2[i+1] < c1[i]:
            return (c1,)

    c1 = list(c1)

    # trim off outer edges that do not intersect and save them
    for i in (0, 2, 4): # check low val edges
        if c2[i] > c1[i]: # keep+remove low side
            n = list(c1)
            n[i+1] = c2[i] - 1 # keep up to just outside c2's left edge
            c1[i] = c2[i] # retain full size including c2's edge
            frags.append(tuple(n))

    for i in (1, 3, 5): # check high val edges
        if c2[i] < c1[i]: # second shape's high side lower than first's low side, keep+remove high side
            n = list(c1)
            n[i-1] = c2[i] + 1 # shaved high end goes to c2's low end but not overlapping
            c1[i] = c2[i] # remaining high end stops 1 toward the low end
            frags.append(tuple(n))

    return tuple(frags)

on = set()
for i, line in enumerate(inp):
    cmd, adding = line[0], line[1:]
    new = set()
    for cube in on:
        scooped = scoop(cube, adding)
        new.update(scooped)
    on = new
    if cmd == 'on':
        on.add(tuple(adding))

for cube in on:
    p2 += vol(cube)
print(f'\rPart 2: {p2}')
