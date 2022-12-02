#!/usr/bin/env python3

import itertools
import re
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

score = 0
with open(input_file) as f:
    for line in f:
        a, b = line.strip().split()
        them = {
            'A': 'rock',
            'B': 'paper',
            'C': 'scissors',
        }[a]
        me = {
            'X': 'rock',
            'Y': 'paper',
            'Z': 'scissors',
        }[b]

        score += {
            'X': 1,
            'Y': 2,
            'Z': 3,
        }[b]

        if me == them:
            score += 3
        elif me == 'scissors' and them == 'paper':
            score += 6
        elif me == 'paper' and them == 'rock':
            score += 6
        elif me == 'rock' and them == 'scissors':
            score += 6

# Part 1

p1 = score
print(f'Part 1: {p1}')

# Part 2
score = 0
with open(input_file) as f:
    for line in f:
        a, b = line.strip().split()
        them = {
            'A': 'rock',
            'B': 'paper',
            'C': 'scissors',
        }[a]
        score += {
            'X': 0,
            'Y': 3,
            'Z': 6,
        }[b]

        if them == 'paper':
            if b == 'X': #lose
                me = 'rock'
            elif b == 'Y': # draw
                me = 'paper'
            else: # win
                me = 'scissors'
        elif them == 'rock':
            if b == 'X': # lose
                me = 'scissors'
            elif b == 'Y': # draw
                me = 'rock'
            else: # win
                me = 'paper'
        elif them == 'scissors':
            if b == 'X': # lose
                me = 'paper'
            elif b == 'Y': # draw
                me = 'scissors'
            else: # win
                me = 'rock'

        score += {
            'rock': 1,
            'paper': 2,
            'scissors': 3,
        }[me]

p2 = score
print(f'Part 2: {p2}')
