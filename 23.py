#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    val = list(map(int, list(f.readline()[:-1])))

def show(data, start):
    n = None
    cups = ''
    while n != start:
        n = start if n is None else n
        print(n, end=' ')
        cups += str(n)
        n = data[n]
    print()
    return cups

def run(cup_list, total_cups, iters):
    mx = max(cup_list)
    data = {}
    for i, v in enumerate(cup_list[:-1]):
        data[v] = cup_list[i+1]

    if total_cups == len(cup_list):
        data[cup_list[i+1]] = cup_list[0]
    else:
        data[cup_list[i+1]] = mx + 1
        data.update({x: x + 1 for x in range(mx + 1, total_cups)})
        mx = total_cups
        data[mx] = cup_list[0]

    next_cup = cup_list[0]
    for move in range(iters):
        if move > 100 and move % 100 == 0:
            print(f'\r{int(move / iters * 100)}%', end='')
        current = next_cup
        new = []
        n = current
        for i in range(3):
            n = data[n]
            new.append(n)
        next_cup = data[new[-1]]
        data[current] = next_cup
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
        data[new[-1]] = data[dest]
        data[dest] = new[0]
    return data

cups = run(val, len(val), 100)
p1 = show(cups, 1)[1:]
print(f'Part 1: {p1}')

cups = run(val, 1000000, 10000000)
p2 = cups[1] * cups[cups[1]]
print(f'\rPart 2: {p2}')
