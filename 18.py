#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

def solve(eq, in_order):
    if in_order:
        for run_op in '+*':
            regex = r'[0-9]+ \+ [0-9]+' if run_op == '+' else r'[0-9]+ \* [0-9]+'
            while re.search(regex, eq):
                gp = re.search(regex, eq).group(0)
                a, b = map(int, gp.split(f' {run_op} '))
                c = a + b if run_op == '+' else a * b
                eq = eq.replace(gp, str(c), 1)
        return eq.lstrip('(').rstrip(')')
    else:
        ch = eq.lstrip('(').rstrip(')').split()
        t = int(ch.pop(0))
        op = None
        for v in ch:
            try:
                v = int(v)
                t = t + v if op == '+' else t * v
            except:
                op = v
        return t

def reduct(eq, in_order):
    gps = re.findall(r'\([0-9 *+]+\)', eq)
    for gp in gps:
        v = solve(gp, in_order)
        eq = eq.replace(gp, str(v), 1)
    return eq

ans = [0, 0] 
with open(input_file) as f:
    for line in f:
        eqs = [line[:-1], line[:-1]]
        if test:
            print()
            print(eqs[0])
        for i, eq in enumerate(eqs):
            while '(' in eq:
                eq = reduct(eq, i)
            a = int(solve(eq, i))
            if test:
                print(a)
            ans[i] += a

p1, p2 = ans
print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
