#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(list(line.rstrip()))

moves = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

keypad1 = {
    (0, 0): '1',
    (1, 0): '2',
    (2, 0): '3',
    (0, 1): '4',
    (1, 1): '5',
    (2, 1): '6',
    (0, 2): '7',
    (1, 2): '8',
    (2, 2): '9',
}

keypad2 = {
    (2, 0): '1',
    (1, 1): '2',
    (2, 1): '3',
    (3, 1): '4',
    (0, 2): '5',
    (1, 2): '6',
    (2, 2): '7',
    (3, 2): '8',
    (4, 2): '9',
    (1, 3): 'A',
    (2, 3): 'B',
    (3, 3): 'C',
    (2, 4): 'D',
}

def run(keypad, x, y):
    code = ''
    for steps in inp:
        for step in steps:
            dx, dy = moves[step]
            nx, ny = x + dx, y + dy
            if keypad.get((nx, ny)):
                x, y = nx, ny
        code += keypad[x, y]
    return code

p1 = run(keypad1, 1, 1)
print(f'Part 1: {p1}')

p2 = run(keypad2, 0, 2)
print(f'Part 2: {p2}')
