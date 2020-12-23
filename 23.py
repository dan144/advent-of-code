#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    val = list(map(int, list(f.readline()[:-1])))

def show(cups, start):
    n = None
    cups_str = ''
    while n != start:
        n = start if n is None else n
        print(n, end=' ')
        cups_str += str(n)
        n = cups[n]
    print()
    return cups_str

def run(cup_list, total_cups, iters):
    mx = max(cup_list)
    cups = {}
    for i, v in enumerate(cup_list[:-1]):
        cups[v] = cup_list[i+1]

    if total_cups == len(cup_list):
        cups[cup_list[i+1]] = cup_list[0]
    else:
        cups[cup_list[i+1]] = mx + 1
        cups.update({x: x + 1 for x in range(mx + 1, total_cups)})
        mx = total_cups
        cups[mx] = cup_list[0]

    next_cup = cup_list[0]
    for move in range(iters):
        if move > 100 and move % 100 == 0:
            print(f'\r{int(move / iters * 100)}%', end='')

        current = next_cup

        move_cups = []
        n = current
        for i in range(3):
            n = cups[n]
            move_cups.append(n)

        # skip the cups being moved
        next_cup = cups[move_cups[-1]]
        cups[current] = next_cup

        # find the destination cup
        dest = current - 1
        while not cups.get(dest) or dest in move_cups:
            dest = (dest - 1) % (mx + 1)

        # point the moved cups to where the destination cup used to point
        cups[move_cups[-1]] = cups[dest]
        # point the destination cup at the moved cups
        cups[dest] = move_cups[0]

    return cups

cups = run(val, len(val), 100)
p1 = show(cups, 1)[1:]
print(f'Part 1: {p1}')

cups = run(val, 1000000, 10000000)
p2 = cups[1] * cups[cups[1]]
print(f'\rPart 2: {p2}')
