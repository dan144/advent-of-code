#!/usr/bin/env python3

from copy import deepcopy

import string
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.strip())

# Part 1
cave = {}
big = set()
small = set()
routes = set()
for line in inp:
    s, e = line.split('-')
    if e != 'start' and s != 'end':
        routes.add((s, e))
    if s != 'start' and e != 'end':
        routes.add((e, s))

    for pos in (s, e):
        if pos in ('start', 'end'):
            continue
        if all(x in string.ascii_lowercase for x in pos):
            small.add(pos)

def remove(s, v):
    for a, b in deepcopy(s):
        if v in (a, b):
            s.remove((a, b))

num_routes = len(routes)

def step(path, routes, visited):
    global paths
    global checked

    if len(path) > num_routes or tuple(path) in paths | checked:
        checked.add(tuple(path))
        return

    n_routes = deepcopy(routes)
    pos = path[-1]

    locs = set()
    for a, b in n_routes:
        if a == pos:
            locs.add(b)

    if all(x in string.ascii_lowercase for x in pos):
        if pos != can_double or (pos == can_double and visited):
            remove(n_routes, pos)
        if pos == can_double:
            visited = True

    for loc in locs:
        if loc == 'end':
            paths.add(tuple(path + ['end']))
            continue

        checked.add(tuple(path))
        step(path + [loc], deepcopy(n_routes), visited)

paths = set()
checked = set()
can_double = None

step(['start'], routes, False)

p1 = len(paths)
print(f'Part 1: {p1}')

# Part 2

paths = set()

# For my input: number of paths when visiting the key node up to twice
s = {
    'yq': 18003,
    'oe': 19462,
    'we': 11019,
    'ys': 7606,
    'wq': 7641,
    'pr': 16771,
    'px': 11720,
    'qk': 3000,
}

# sum of above, less duplicated paths (each count includes visiting that node 1 or 0 times)
# realized that when qk was 3000; qk only adjacent to yq in the input and 3000 is part 1 solution
# qk can only be visited when yq is doubled, otherwise never visited
# 
# Originally computed this by running a copy of this that only doubled a single thread from a cli arg
# Essentially a threaded solution but without actually using threading
if not test:
    p2 = sum(s.values()) - (3000 * len(s.values())) + 3000
    print('Part 2:', p2)
    print('(Hardcoded for my input; computing on input file now)')

# This solution works, just really slowly for actual inputs
for x in small:
    if not test:
        print(x)
    checked = set()
    can_double = x
    step(['start'], routes, False)

p2 = len(paths)
print(f'Part 2: {p2}')
