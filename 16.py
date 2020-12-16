#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 1

inp = []
fields = []
my_ticket = None
all_tickets = []
with open(input_file) as f:
    in_fields = True
    for line in f:
        if line == '\n':
            in_fields = False
        elif in_fields:
            field, mn1, mx1, mn2, mx2 = re.search(r'([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9-]+)-([0-9-]+)', line).groups()
            r1 = set(range(int(mn1), int(mx1) + 1))
            r2 = set(range(int(mn2), int(mx2) + 1))
            fields.append((field, r1.union(r2)))
        else:
            try:
                nums = list(map(int, line.split(',')))
                if my_ticket is None:
                    my_ticket = nums
                else:
                    all_tickets.append(nums)
            except ValueError:
                pass

all_valid = set()
for field, v in fields:
    all_valid |= v

discard = set()
for i, ticket in enumerate(all_tickets):
    for value in ticket:
        if value not in all_valid:
            p1 += value
            discard.add(i)

for k in sorted(discard, reverse=True):
    all_tickets.pop(k)

valids = []
for i in range(len(fields)):
    valids.append([True] * len(my_ticket))

# all ticket must be valid, so any invalid value invalidates that slot from being a field
for ticket in all_tickets:
    for i, value in enumerate(ticket):
        for j, (_, valid) in enumerate(fields):
            if value not in valid:
                valids[i][j] = False

i = 0
solos = set()
while solos != set(range(len(valids))):
    row = valids[i]
    count = row.count(True)
    if count == 1:
        solos.add(i)
        idx = row.index(True)
        for j, valid in enumerate(valids):
            if i == j:
                continue
            valid[idx] = False

    i = (i + 1) % len(valids)

for i, row in enumerate(valids):
    idx = row.index(True)
    if fields[idx][0].startswith('departure'):
        p2 *= my_ticket[i]

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
