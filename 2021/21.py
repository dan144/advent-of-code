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

p1 = 0
p2 = 0

pos = []
with open(input_file) as f:
    for line in f:
        n = int(re.findall(r'[0-9]+', line)[-1])
        pos.append(n)

# For part 2
games = {
    tuple(pos) + (0, 0, False): 1,
}

# Part 1
scores = [0] * len(pos)
rolls = 0
while all(x < 1000 for x in scores):
    for player in range(len(pos)):
        for roll in range(3):
            rolls += 1
            r_v = (rolls - 1) % 100 + 1
            pos[player] += r_v
        pos[player] = (pos[player] - 1) % 10 + 1
        scores[player] += pos[player]
        if scores[player] >= 1000:
            break

p1 = rolls * sorted(scores)[0]
print(f'Part 1: {p1}')

# Part 2
# (p1 position, p2 position, p1 score, p2 score, is p2's turn?): num games
wins = {
    1: 0,
    2: 0
}

dist = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}

while games:
    new = {}
    for (p1p, p2p, p1s, p2s, turn), c in games.items():
        for dp, n in dist.items():
            if turn:
                p = p2p
            else:
                p = p1p
            p = (p + dp - 1) % 10 + 1

            if turn:
                s = p2s + p
                if s >= 21:
                    wins[2] += c * n
                else:
                    k = (p1p, p, p1s, s, False)
                    if k not in new:
                        new[k] = 0
                    new[k] += c * n
            else:
                s = p1s + p
                if s >= 21:
                    wins[1] += c * n
                else:
                    k = (p, p2p, s, p2s, True)
                    if k not in new:
                        new[k] = 0
                    new[k] += c * n
    games = new
p2 = sorted(wins.values())[1]
print(f'Part 2: {p2}')
