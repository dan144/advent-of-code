#!/usr/bin/env python3

import hashlib
import sys

from collections import OrderedDict

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p2 = 0

with open(input_file) as f:
    prefix = f.readline().rstrip()

prefix = prefix.encode()

moves = OrderedDict({
    b'U': (0, -1),
    b'D': (0, 1),
    b'L': (-1, 0),
    b'R': (1, 0),
})

def run(locs, dest, terminate):
    global p2

    new_locs = set()
    if not locs:
        return new_locs

    for (x, y), path in locs:
        if (x, y) == dest:
            # path ends once you find the vault
            continue
        digest = hashlib.md5(prefix + path).hexdigest()
        doors = []
        for i, (move, (dx, dy)) in enumerate(moves.items()):
            nx, ny = x + dx, y + dy
            doors.append(digest[i] in 'bcdef')
            if 0 <= nx <= dest[0] and 0 <= ny <= dest[1]:
                if digest[i] in 'bcdef':
                    # door is open
                    new_locs.add(((nx, ny), path + move))

    if dest in {loc[0] for loc in new_locs}:
        if terminate:
            return new_locs
        else:
            p2 = max(p2, len([loc[1] for loc in new_locs if loc[0] == dest][0]))

    return run(new_locs, dest, terminate)

dest = (3, 3)
locs = run({((0, 0), b'')}, dest, True)
assert locs
p1 = [loc[1] for loc in locs if loc[0] == dest][0].decode()
print(f'Part 1: {p1}')

p2 = 0
locs = run({((0, 0), b'')}, dest, False)
assert not locs
print(f'Part 2: {p2}')
