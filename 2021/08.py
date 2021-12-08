#!/usr/bin/env python3

import itertools
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file) as f:
    inp = utils.load_split_lines(f) # asdf asdf asdf ...

# Part 1
segs = []
for line in inp:
    segs.append([])
    pipe = False # only monitor things after |
    for v in line:
        if v == '|':
            pipe = True
        else:
            if pipe and len(v) in {2, 4, 3, 7}:
                p1 += 1
            segs[-1].append(v)
print(f'Part 1: {p1}')

# Part 2

for line in segs:
    for p in itertools.permutations('abcdefg'): # try all permutations of segments
        valid = True
        guesses = {}
        for num in line:
            num_l = len(num)
            num_s = set(num)

            if num_l == 2: # 1
                g = {p[2], p[5]}
                if g != num_s:
                    valid = False
                else:
                    guesses[1] = g
            elif num_l == 3: # 7
                g = {p[0], p[2], p[5]}
                if g != num_s:
                    valid = False
                else:
                    guesses[7] = g
            elif num_l == 4: # 4
                g = {p[x] for x in (1, 2, 3, 5)}
                if g != num_s:
                    valid = False
                else:
                    guesses[4] = g
            elif num_l == 7: # 8
                guesses[8] = num_s
            elif num_l == 5: # 2,3,5
                g2 = {p[x] for x in (0, 2, 3, 4, 6)}
                g3 = {p[x] for x in (0, 2, 3, 5, 6)}
                g5 = {p[x] for x in (0, 1, 3, 5, 6)}
                if g2 == num_s: # 2
                    guesses[2] = g2
                elif g3 == num_s: # 3
                    guesses[3] = g3
                elif g5 == num_s: # 5
                    guesses[5] = g5
                else:
                    valid = False
            elif num_l == 6: # 0,6,9
                g0 = {p[x] for x in (0, 1, 2, 4, 5, 6)}
                g6 = {p[x] for x in (0, 1, 3, 4, 5, 6)}
                g9 = {p[x] for x in (0, 1, 2, 3, 5, 6)}
                if g0 == num_s: # 0
                    guesses[0] = g0
                elif g6 == num_s: # 6
                    guesses[6] = g6
                elif g9 == num_s: # 9
                    guesses[9] = g9
                else:
                    valid = False

            if not valid:
                break

        if len(guesses.keys()) != 10:
            continue # didn't match all ten, so must be wrong

        output = 0
        for num in line[-4:]: # sum up the values of the last 4
            output *= 10
            for k, v in guesses.items():
                if v == set(num):
                    output += k
        p2 += output
        break

print(f'Part 2: {p2}')
