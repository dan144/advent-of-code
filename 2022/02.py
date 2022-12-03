#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

moves = ['rock', 'paper', 'scissors']

with open(input_file) as f:
    for line in f:
        a, b = line.strip().split()
        them = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}[a]
        me = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}[b]

        p1 += {'X': 1, 'Y': 2, 'Z': 3}[b]

        if me == them:
            p1 += 3
        elif (moves.index(me) - 1) % 3 == moves.index(them):
            p1 += 6

print(f'Part 1: {p1}')

# Part 2
with open(input_file) as f:
    for line in f:
        a, b = line.strip().split()
        them = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}[a]

        if b == 'X': # lose
            me = moves[(moves.index(them) - 1) % 3]
        elif b == 'Y': # draw
            me = them
        else: # win
            me = moves[(moves.index(them) + 1) % 3]

        p2 += {'X': 0, 'Y': 3, 'Z': 6}[b]
        p2 += {'rock': 1, 'paper': 2, 'scissors': 3}[me]

print(f'Part 2: {p2}')
