#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    val = list(map(int, list(f.readline()[:-1])))

mx = max(val)
data = {}
for i, v in enumerate(val[:-1]):
    data[v] = val[i+1]
data[val[i+1]] = mx + 1
go_to = 1000000
data.update({x: x + 1 for x in range(mx + 1, go_to)})
data[go_to] = val[0]
if go_to < 100:
    print(data)
mx = go_to

def show(start):
    n = None
    while n != start:
        n = start if n is None else n
        print(n, end=' ')
        n = data[n]
    print()

next_cup = val[0]
for move in range(10000000):
    if move % 10000 == 0:
        print('Move:', move)
    current = next_cup
    # show(current)
    #print(f'({current})')
    new = []
    n = current
    for i in range(3):
        n = data[n]
        new.append(n)
    next_cup = data[new[-1]]
    data[current] = next_cup
    #print('pick up:', new)
    dest = current
    while True:
        try:
            dest = dest - 1
            if data[dest] and dest not in new:
                break
        except KeyError:
            dest -= 1
            if dest < 0:
                dest = mx + 1
    #print('destination:', dest)
    data[new[-1]] = data[dest]
    data[dest] = new[0]
    # input()

# idx = val.index(1)
# p1 = ''.join(map(str, val[idx+1:] + val[:idx]))
# show(1)
print(f'Part 1: {p1}')

print(data[1], data[data[1]])
p2 = data[1] * data[data[1]]
print(f'Part 2: {p2}')
