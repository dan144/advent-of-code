#!/usr/bin/env python3

import sys

import utils
# get_grid_edges - min_x, min_y, max_x, max_y
# display_grid((y, x) grid) - display values in 2D map grid

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

def build_grid():
    grid = {}
    with open(input_file) as f:
        for line in f:
            coords = line.split('->')
            prev = None
            for coord in coords:
                nx, ny = map(int, coord.strip().split(','))
                if prev is not None:
                    x, y = prev
                    if x == nx and y != ny:
                        for my in range(min(y, ny), max(y, ny) + 1):
                            grid[my, x] = '#'
                    elif y == ny and x != nx:
                        for mx in range(min(x, nx), max(x, nx) + 1):
                            grid[y, mx] = '#'
                    else:
                        assert x == nx and y == ny # single point; skip
                prev = (nx, ny)
    return grid
    
grid = build_grid()
min_y, min_x, max_y, max_x = utils.get_grid_edges(grid)
#utils.display_grid(grid)


# Part 1

def run(part):
    score = 0
    while True:
        grain = (0, 500)
        falling = True
        while falling:
            if grain[0] >= max_y:
                # this grain has reached infinity
                assert part == 1
                return score
            for dy in [0, -1, 1]:
                n = (grain[0] + 1, grain[1] + dy)
                if grid.get(tuple(n), '.') not in '#o':
                    grain = n
                    break # can fall this way
            else:
                grid[grain] = 'o'
                score += 1
                falling = False
        if grid.get((0, 500)) == 'o':
            assert part == 2 # technically could happen in part 1
            return score

p1 = run(1)
print(f'Part 1: {p1}')

# Part 2

grid = build_grid()
dx = max_x - min_x
max_y += 2

for x in range(min_x - 10 * dx, max_x + 10 * dx):
    grid[max_y, x] = '#'
p2 = run(2)
print(f'Part 2: {p2}')
