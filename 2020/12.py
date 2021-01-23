#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    for line in f:
        inp.append((line[0], int(line[1:])))

dirs = 'NESW'
moves = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
    'R': 1,
    'L': -1,
}

direc = 1
x, y = 0, 0
for act, dist in inp:
    if act in 'LR':
        direc = (direc + moves[act] * dist // 90) % 4
    else:
        if act == 'F':
            act = dirs[direc]
        dx, dy = moves[act]
        x += dx * dist
        y += dy * dist

p1 = utils.manh((x, y))
print(f'Part 1: {p1}')

direc = 1
x, y = 0, 0
wx, wy = 10, 1
for act, dist in inp:
    if act in 'LR':
        for _ in range(dist // 90):
            wx, wy = (wy, -1 * wx) if act == 'R' else (-1 * wy, wx)
    elif act == 'F':
        x += dist * wx
        y += dist * wy
    else:
        dx, dy = moves[act]
        wx += dx * dist
        wy += dy * dist

p2 = utils.manh((x, y))
print(f'Part 2: {p2}')
