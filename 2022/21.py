#!/usr/bin/env python3

import re
import sys

from copy import deepcopy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

o_monkeys = {}
with open(input_file) as f:
    for line in f:
        monkey, equation = re.search(r'([a-z]+): (.*)', line.strip()).groups()
        try:
            equation = int(equation)
        except Exception:
            pass

        o_monkeys[monkey] = equation

# Part 1

monkeys = deepcopy(o_monkeys)
while str in map(lambda x: type(x), monkeys.values()):
    for monkey in monkeys.keys():
        if isinstance(monkeys[monkey], int):
            continue
        equation = monkeys[monkey]
        for sub in re.findall(r'[a-z]{4}', equation):
            if isinstance(monkeys[sub], str):
                break
            equation = equation.replace(sub, str(monkeys[sub]))
        else:
            monkeys[monkey] = int(eval(equation))

p1 = monkeys['root']
print(f'Part 1: {p1}')

# Part 2

root = o_monkeys['root'].replace('+', '==')
o_monkeys['humn'] = 'humn'
while set(re.findall(r'([a-z]{4})', root)) != {'humn'}:
    needs = re.findall(r'([a-z]{4})', root)
    for n in needs:
        if isinstance(o_monkeys[n], int) or o_monkeys[n] == 'humn':
            root = root.replace(n, str(o_monkeys[n]))
        else:
            root = root.replace(n, f'({o_monkeys[n]})')

root = root.replace(' ', '')
while n := re.search(r'\(\d+[-+\*/]\d+\)', root):
    n = n.group(0)
    root = root.replace(n, str(int(eval(n))))

while re.fullmatch(r'humn==\d+', root) is None:
    if g := re.fullmatch(r'\((\d+)\+(.*)\)==(\d+)', root):
        root = f'{g.groups()[1]}=={int(g.groups()[2]) - int(g.groups()[0])}'
    elif g := re.fullmatch(r'\((\d+)-(.*)\)==(\d+)', root):
        root = f'{g.groups()[1]}=={int(g.groups()[0]) - int(g.groups()[2])}'
    elif g := re.fullmatch(r'\((\d+)\*(.*)\)==(\d+)', root):
        root = f'{g.groups()[1]}=={int(g.groups()[2]) // int(g.groups()[0])}'
    elif g := re.fullmatch(r'\((\d+)/(.*)\)==(\d+)', root):
        root = f'{g.groups()[1]}=={int(g.groups()[0]) // int(g.groups()[2])}'
    elif g := re.fullmatch(r'\((.*)\+(\d+)\)==(\d+)', root):
        root = f'{g.groups()[0]}=={int(g.groups()[2]) - int(g.groups()[1])}'
    elif g := re.fullmatch(r'\((.*)-(\d+)\)==(\d+)', root):
        root = f'{g.groups()[0]}=={int(g.groups()[2]) + int(g.groups()[1])}'
    elif g := re.fullmatch(r'\((.*)\*(\d+)\)==(\d+)', root):
        root = f'{g.groups()[0]}=={int(g.groups()[2]) // int(g.groups()[1])}'
    elif g := re.fullmatch(r'\((.*)/(\d+)\)==(\d+)', root):
        root = f'{g.groups()[0]}=={int(g.groups()[1]) * int(g.groups()[2])}'

p2 = root.split('==')[1]
print(f'Part 2: {p2}')
