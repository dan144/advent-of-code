#!/usr/bin/python3.6

import json
import re

with open('input/12', 'r') as f:
    inp = f.read()

nums = re.findall(r'-?\d+', inp)
ans = sum(map(int, nums))
print(f'Part 1: {ans}')

with open('input/12', 'r') as f:
    inp = json.load(f)

total = 0
def parse(d):
    global total

    if isinstance(d, list):
        for x in d:
            parse(x)
    elif isinstance(d, dict):
        if not 'red' in d.values():
            for v in d.values():
                parse(v)
    else:
        try:
            total += int(d)
        except ValueError:
            pass

parse(inp)
print(f'Part 2: {total}')
