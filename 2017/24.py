#!/usr/bin/env python3

import sys

from copy import deepcopy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = [0, 0]

ports = []
with open(input_file) as f:
    for line in f:
        ports.append(tuple(sorted(map(int, line.rstrip().split('/')))))

def value(ports):
    total = 0
    for a, b in ports:
        total += a + b
    return total

def dig(ports, remaining):
    global p1
    global p2

    if not remaining:
        return ports

    for a, b in remaining:
        n = None
        if ports[-1][1] == a:
            n = (a, b)
        elif ports[-1][1] == b:
            n = (b, a)

        if n:
            d_ports = deepcopy(ports) + [n]
            d_remaining = deepcopy(remaining)
            d_remaining.remove((a, b))

            r_ports = dig(d_ports, d_remaining)

            v = value(r_ports)
            if v > p1:
                p1 = v

            if len(r_ports) >= p2[0]:
                p2[1] = v if len(r_ports) > p2[0] else max(v, p2[1])
                p2[0] = len(r_ports)

            print(f'\r{p1} {p2[1]}', end=' ')
    return ports

for port in ports:
    if port[0] != 0:
        continue
    remain = set(ports)
    remain.remove(port)
    dig([port], remain)

print(f'\nPart 1: {p1}')
print(f'Part 2: {p2[1]}')
