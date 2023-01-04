#!/usr/bin/env python3

import sys

import utils
### available functions:
# get_grid_edges - min_x, min_y, max_x, max_y

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    for line in f:
        jets = list(line.strip())

# Part 1

shape_coords = (
    (
        (3, 4), (4, 4), (5, 4), (6, 4)
    ), (
        (3, 5), (4, 5), (5, 5), (4, 4), (4, 6)
    ), (
        (3, 4), (4, 4), (5, 4), (5, 5), (5, 6)
    ), (
        (3, 4), (3, 5), (3, 6), (3, 7)
    ), (
        (3, 4), (4, 4), (3, 5), (4, 5)
    )
)

grid = {}
for y in range(1, 8):
    grid[y, 0] = '-'
grid[0, 0] = '+'
grid[8, 0] = '+'
min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)

moveidx = 0
diffs = ''
vals = []
for b in range(5000):
    o = max_y
    vals.append(o)
    min_x, min_y, max_x, max_y = utils.get_grid_edges(grid)
    diffs += str(max_y - o)
    new_coords = list(map(list, shape_coords[b % 5]))

    print(f'\rBlock {b}', end='')

    for c in new_coords:
        c[1] += max_y

    while True:
        move = jets[moveidx % len(jets)]
        moveidx += 1

        # sideways
        can_move = True
        for (x, y) in new_coords:
            if move == '<':
                x -= 1
            else:
                x += 1
            if x in {0, 8} or grid.get((x, y)):
                can_move = False
                break
        if can_move:
            for c in new_coords:
                c[0] += 1 if move == '>' else -1

        # down
        can_move = True
        for (x, y) in new_coords:
            if grid.get((x, y-1)):
                can_move = False
                break
        for c in new_coords:
            if can_move:
                c[1] -= 1
            else:
                grid[tuple(c)] = '#'
        if not can_move:
            break

print()

p1 = vals[2022]
print(f'Part 1: {p1}')

for j in range(5000, 1000, -1):
    l = len(diffs)
    rest, find = diffs[:l - j], diffs[l - j:]
    if rest.endswith(find):
        f = len(find)
        x = sum([int(x) for x in find])
        print(f'Pattern is {f} long and increments {x}')
        n = 1000000000000 // f
        s = 1000000000000 % f + 1
        print(f'Repeats {n} times and starts at pos {s} ({vals[s]})')
        p2 = x * n + vals[s]
        print(f'Part 2: {p2}')
        break
else:
    assert False, 'Failed to solve part 2'
