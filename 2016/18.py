#!/usr/bin/env python3

import sys

from copy import copy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    row = [x == '^' for x in f.readline().rstrip()]

def run(row, n_row):
    total = len(row) - sum(row)
    for y in range(1, n_row):
        new_row = []
        for x in range(len(row)):
            l = row[x - 1] if x > 0 else False
            c = row[x]
            r = row[x + 1] if x < len(row) - 1 else False

            m = any((
                l and c and not r,
                c and r and not l,
                l and not r and not c,
                r and not l and not c,
            ))

            new_row.append(m)

        total += len(row) - sum(row)
        row = new_row
    return total


p1 = run(copy(row), 10 if test else 40)
print(f'Part 1: {p1}')
p2 = run(row, 10 if test else 400000)
print(f'Part 2: {p2}')
