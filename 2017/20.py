#!/usr/bin/env python3

import re
import sys

from copy import deepcopy

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

particles = []
with open(input_file) as f:
    for line in f:
        p, v, a = re.findall(r'-?\d+,-?\d+,-?\d+', line)
        x = []
        for arr in (p, v, a):
            x.append(list(map(int, arr.split(','))))
        particles.append(x)

o_particles = deepcopy(particles)

for _ in range(1000):
    closest = None
    closest_dist = float('inf')
    for i, n in enumerate(particles):
        p, v, a = n
        for j in range(len(p)):
            v[j] += a[j]
            p[j] += v[j]
        man_dist = utils.manh(p)
        if man_dist < closest_dist:
            closest = i
            closest_dist = man_dist

p1 = closest
print(f'Part 1: {p1}')
particles = deepcopy(o_particles)

consec = [0, len(particles)]
while consec[0] < 100:
    for i, n in enumerate(particles):
        p, v, a = n
        for j in range(len(p)):
            v[j] += a[j]
            p[j] += v[j]
    to_remove = set()
    for i, n in enumerate(particles):
        for j, n2 in enumerate(particles):
            if i == j:
                continue
            if n[0] == n2[0]:
                to_remove.update({i, j})
    for p in sorted(to_remove, reverse=True):
        particles.pop(p)

    n = len(particles)
    if n == consec[1]:
        consec[0] += 1
    else:
        consec = [0, n]

p2 = len(particles)
print(f'Part 2: {p2}')
