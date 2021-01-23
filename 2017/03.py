#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    goal = int(f.readline().rstrip())

back_moves = {
    0: (-1, 0),
    1: (0, -1),
    2: (1, 0),
    3: (0, 1),
}

s = 1
while s ** 2 < goal:
    s += 2
x, y = s // 2, s // 2

n = s ** 2
width = s - 1

step = 0
direction = 0
while n > goal:
    n -= 1

    if step and step % width == 0:
        direction += 1
    step += 1

    dx, dy = back_moves[direction]
    x += dx
    y += dy

p1 = utils.manh((0, 0), (x, y))
print(f'Part 1: {p1}')

moves = {
    0: (0, -1),
    1: (-1, 0),
    2: (0, 1),
    3: (1, 0),
}
grid = {(0, 0): 1}
x, y = 1, 0
ring = 1
step = 0
direction = 0
while True:
    width = ring * 2

    step += 1
    s = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            s += grid.get((x + dx, y + dy), 0)
    grid[x, y] = s
    if s > goal:
        p2 = s
        break

    if x == ring and y == ring:
        x += 1
        ring += 1
        step = 0
        direction = 0
        continue

    if step % width == 0:
        direction += 1

    dx, dy = moves[direction % 4]
    x += dx
    y += dy
    assert (x, y) not in grid

print(f'Part 2: {p2}')
