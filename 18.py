#!/usr/bin/env python3

import re
import sys

from computer import parse, run

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

def solve(eq):
    for run_op in '+*':
        regex = r'[0-9]+ \+ [0-9]+' if run_op == '+' else r'[0-9]+ \* [0-9]+'
        while re.search(regex, eq):
            gp = re.search(regex, eq).group(0)
            # print(gp)
            a, b = map(int, gp.split(f' {run_op} '))
            c = a + b if run_op == '+' else a * b
            eq = eq.replace(gp, str(c), 1)


    # t = None
    # op = None
    # for v in eq.lstrip('(').rstrip(')').split():
    #     if t is None:
    #         t = int(v)
    #         continue
    #     try:
    #         v = int(v)
    #         t = t + v if op == '+' else t * v
    #     except:
    #         op = v

    return eq.lstrip('(').rstrip(')')

def reduct(eq):
    gps = re.findall(r'\([0-9 *+]+\)', eq)
    for gp in gps:
        v = solve(gp)
        eq = eq.replace(gp, v)
    return eq

with open(input_file) as f:
    for line in f:
        eq = line[:-1]
        while '(' in eq:
            eq = reduct(eq)
        p1 += int(solve(eq))

print(f'Part 1: {p1}')

print(f'Part 2: {p2}')
