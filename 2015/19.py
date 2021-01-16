#!/usr/bin/python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

reps = {}
with open(input_file) as f:
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

p1 = len(ans)
print(f'Part 1: {p1}')

# invert to backtrace
back_reps = {}
for f, ts in reps.items():
    for t in ts:
        assert t not in back_reps
        back_reps[t] = f

s = ''.join(s)
p2 = 0
while s != 'e':
    # search longest to shortest replacement
    for f, t in sorted(back_reps.items(), key=lambda x: len(x[0]), reverse=True):
        if t == 'e' and s != f:
            continue
        while f in s:
            match = re.search(f, s)
            p2 += 1
            s = s[:match.start(0)] + t + s[match.end(0):]
            break

print(f'Part 2: {p2}')
