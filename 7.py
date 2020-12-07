#!/usr/bin/env python3

import re
import sys

from copy import copy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

inp = []
with open(input_file, 'r') as f:
    for line in f.read().splitlines():
        inp.append(line)

holder = re.compile(r'[a-z]+ [a-z]+')
held = re.compile(r'([0-9]+) ([a-z ]+) bags?')
bags = {}
for line in inp:
    h = holder.search(line).group()
    bags[h] = {}
    if 'no other' not in line:
        g = held.findall(line)
        for n, t in g:
            bags[h][t] = int(n)

check = set()
for color in bags.keys():
    check.add(color)

checked = set()

def dig(color):
    if color not in bags.keys():
        return False

    colors = {c for c, n in bags[color].items()}
    if 'shiny gold' in colors:
        return True

    for color in colors:
        if dig(color):
            return True
    return False

for color in check:
    p1 += dig(color) != 0

print(f'Part 1: {p1}')

def contain(color, x):
    t = x
    for c, n in bags[color].items():
        t += x * contain(c, n)
    return t

p2 = contain('shiny gold', 1) - 1

print(f'Part 2: {p2}')
