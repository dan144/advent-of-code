#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

monkeys = {}
with open(input_file) as f:
    for line in f:
        monkey, equation = re.search(r'([a-z]+): (.*)', line.strip()).groups()
        try:
            equation = int(equation)
        except Exception:
            pass

        monkeys[monkey] = equation

# Part 1

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

print(f'Part 2: {p2}')
