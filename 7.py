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

# ex: light red bags contain 1 bright white bag, 2 muted yellow bags.
holder_re = re.compile(r'[a-z]+ [a-z]+') # line starts with "<adjective> <color> bags"
held_re = re.compile(r'([0-9]+) ([a-z ]+) bags?') # every occurrence of "<n> <adjective> bag(s)"

bags = {}
for line in inp:
    holder = holder_re.search(line).group()
    bags[holder] = {}
    if 'no other' not in line:
        for n, t in held_re.findall(line):
            bags[holder][t] = int(n)

def dig(color):
    colors = bags[color].keys()
    if 'shiny gold' in colors:
        return True

    for color in colors:
        if dig(color):
            return True
    return False

for color in bags.keys():
    p1 += dig(color)
print(f'Part 1: {p1}')

def contain(color, num):
    total = num
    for c, n in bags[color].items():
        # this level has the num of these bags times what they contain
        total += num * contain(c, n)
    return total

p2 = contain('shiny gold', 1) - 1
print(f'Part 2: {p2}')
