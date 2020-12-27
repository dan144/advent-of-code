#!/usr/bin/python3.6

import re

reps = {}
with open('input/19', 'r') as f:
    for line in f:
        if line == '\n':
            continue
        line = line.split(' => ')
        if len(line) == 2:
            k, v = line
            if k not in reps:
                reps[k] = []
            reps[k].append(v.strip())
        else:
            s = list(line[0].strip())

ans = set()
for k, vs in reps.items():
    matches = re.finditer(k, ''.join(s))
    for match in matches:
        for v in vs:
            new = ''.join(s[:match.start(0)] + list(v) + s[match.end(0):])
            ans.add(new)

print(f'Part 1: {len(ans)}')
