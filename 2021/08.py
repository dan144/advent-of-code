#!/usr/bin/env python3

import itertools
import re
import sys

import utils
### available functions:
# get_grid_edges: min_x, min_y, max_x, max_y
# display_grid
# find_dist(grid, 0, (x,y) start, (x,y) dest) - open=True, wall=False
# manh(p1[, p2]) - n-dim Manhattan dist; omit p2 for dist from origin
# is_prime

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    inp = utils.load_split_lines(f) # asdf asdf asdf ...

# Part 1
segs = []
seen = set()
for line in inp:
    segs.append(([], []))
    pipe = False
    for v in line:
        if v == '|':
            pipe = True
        else:
            if pipe:
                seen.add(v)
                segs[-1][1].append(v)
                if len(v) in {2, 4, 3, 7}:
                    p1 += 1
            else:
                segs[-1][0].append(v)
print(f'Part 1: {p1}')

# Part 2

# 2 5
# 3 5
# 5 5

# 0 6
# 6 6
# 9 6

# 1 2
# 4 4
# 7 3
# 8 7

for line in segs:
    for p in itertools.permutations('abcdefg'):
        valid = True
        guesses = {}
        for num in line[0] + line[1]:
            if len(num) == 2: # 1
                g = {p[2], p[5]}
                if g != set(num):
                    valid = False
                #elif guesses.get(1) != g:
                    pass #valid = False
                else:
                    guesses[1] = g
            elif len(num) == 3: # 7
                g = {p[0], p[2], p[5]}
                if g != set(num):
                    valid = False
                #elif guesses.get(7) != g:
                    pass #valid = False
                else:
                    guesses[7] = g
            elif len(num) == 4: # 4
                g = {p[x] for x in (1, 2, 3, 5)}
                if g != set(num):
                    valid = False
                #elif guesses.get(4) != g:
                    pass #valid = False
                else:
                    guesses[4] = g
            elif len(num) == 7: # 8
                guesses[8] = set(num)
            elif len(num) == 5: # 2,3,5
                g2 = {p[x] for x in (0, 2, 3, 4, 6)}
                g3 = {p[x] for x in (0, 2, 3, 5, 6)}
                g5 = {p[x] for x in (0, 1, 3, 5, 6)}
                if g2 == set(num): # 2
                    guesses[2] = g2
                elif g3 == set(num): # 3
                    guesses[3] = g3
                elif g5 == set(num):
                    guesses[5] = g5
                else:
                    valid = False
            elif len(num) == 6: # 0,6,9
                g0 = {p[x] for x in (0, 1, 2, 4, 5, 6)}
                g6 = {p[x] for x in (0, 1, 3, 4, 5, 6)}
                g9 = {p[x] for x in (0, 1, 2, 3, 5, 6)}
                if g0 == set(num): # 0
                    guesses[0] = g0
                elif g6 == set(num): # 6
                    guesses[6] = g6
                elif g9 == set(num): # 9
                    guesses[9] = g9
                else:
                    valid = False
            if valid == False:
                break
        if len(guesses.keys()) != 10:
            continue # wrong

        output = 0
        for num in line[1]:
            output *= 10
            for k, v in guesses.items():
                if v == set(num):
                    output += k
        p2 += output

print(f'Part 2: {p2}')
