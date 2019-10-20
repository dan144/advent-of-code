#!/usr/bin/python3

import re

ing = []
with open('input/15', 'r') as f:
    for line in f:
        m = re.search(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)
        g = list(m.groups())
        for i in range(1, 6):
            g[i] = int(g[i])
        ing.append(g)

m_1 = 0
m_2 = 0
for a in range(101):
    for b in range(0, 101-a):
        for c in range(0, 101-a-b):
            for d in range(0, 101-a-b-c):
                v = [0] * 5
                e = (a,b,c,d)
                for f in range(4):
                    for i in range(5):
                        v[i] += e[f] * ing[f][i+1]
                if min(v[:4]) <= 0:
                    continue
                m_1 = max(m_1, v[0] * v[1] * v[2] * v[3])
                if v[4] != 500:
                    continue
                m_2 = max(m_2, v[0] * v[1] * v[2] * v[3])
print('Part 1: {}'.format(m_1))
print('Part 2: {}'.format(m_2))
