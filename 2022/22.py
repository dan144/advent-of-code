#!/usr/bin/env python3

import itertools
import re
import sys

import utils
### available functions:
# get_grid_edges - min_x, min_y, max_x, max_y
# display_grid((y, x) grid) - display values in 2D map grid
# find_dist(grid, 0, (x,y) start, (x,y) dest) - open=True, wall=False
# find_cheapest(grid, (y,x) start, (y,x) end) - grid of ints, finds cheapest path from start to end, returns cost dist
# transpose_grid(grid) - swap key values from (x, y) to (y, x) and back
# manh(p1[, p2]) - n-dim Manhattan dist; omit p2 for dist from origin
# is_prime
# adjs - set of dx,dy values for LRUD adjacencies
# diags - set of dx,dy values for diagonals
# all_dirs set of dx,dy values for all 8 surrounding values

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p2 = 0

lines = []
done = False
with open(input_file) as f:
    for line in f:
        line = line.rstrip()
        if not line:
            done = True
            grid = utils.parse_grid(lines)
        elif done is False:
            lines.append(line)
        else:
            ins = re.findall(r'([LR]|\d+)', line)

assert line == ''.join(ins)
# Part 1

min_y, min_x, max_y, max_x = utils.get_grid_edges(grid)
y = min_y
for x in range(min_x, max_x + 1):
    if grid.get((y, x)) == '.':
        break
else:
    assert False

deltas = {
    0: (1, 0),
    1: (0, 1),
    2: (-1, 0),
    3: (0, -1),
}

grid[y, x] = '>'
facing = 0 # right 0, down 1, left 2, up 3
for i in ins:
    assert grid[y, x] in '.><^v'
    if i in 'LR':
        facing += 1 if i == 'R' else -1
        facing = facing % 4
        grid[y, x] = '>v<^'[facing]
    else:
        d = deltas[facing]
        for _ in range(int(i)):
            nx = x + d[0]
            ny = y + d[1]
            n = grid.get((ny, nx), ' ')
            if n in ' ': # wrap
                if facing == 0: # right
                    nx = min_x
                elif facing == 1: # down
                    ny = min_y
                elif facing == 2: # left
                    nx = max_x
                elif facing == 3: # up
                    ny = max_y
                else:
                    assert False, f'Facing is {facing}'

                while (n := grid.get((ny, nx), ' ')) in ' ':
                    nx += d[0]
                    ny += d[1]

            if n == '#': # stop
                break
            elif n in '.<>v^': # go
                y, x = ny, nx
            else:
                utils.display_grid(grid)
                assert False, f'Found a {n} at {x}, {y}'

            grid[y, x] = '>v<^'[facing]
        if test:
            utils.display_grid(grid)
            print()
            input()

print(y + 1, x + 1, facing)
p1 = 1000 * (y + 1) + 4 * (x + 1) + facing
#utils.display_grid(grid)
print(f'Part 1: {p1}')

# Part 2

print(f'Part 2: {p2}')
