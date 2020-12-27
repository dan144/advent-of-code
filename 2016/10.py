#!/usr/bin/env python3

import re
import sys

from copy import copy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

bots = {}
gives = []
with open(input_file) as f:
    for line in f:
        if line.startswith('value'):
            value, bot = map(int, re.findall(r'\d+', line))
            if bot not in bots:
                bots[bot] = [value]
            else:
                bots[bot].append(value)
        else:
            gives.append(re.findall(r'\d+|output|bot', line)[1:])

outputs = {}
while gives:
    for give in copy(gives):
        bot, type1, value1, type2, value2 = give
        bot = int(bot)
        if len(bots.get(bot, [])) != 2:
            continue
        values = sorted(bots[bot])
        for t, v in ((type1, value1), (type2, value2)):
            v = int(v)
            if t == 'bot':
                if v not in bots:
                    bots[v] = []
                bots[v].append(values.pop(0))
            else:
                outputs[v] = values.pop(0)
        gives.remove(give)

if test:
    print('Bot 2:', bots[2])
else:
    p1 = {tuple(sorted(v)): k for k, v in bots.items()}[17, 61]
    print(f'Part 1: {p1}')

p2 = outputs[0] * outputs[1] * outputs[2]
print(f'Part 2: {p2}')
