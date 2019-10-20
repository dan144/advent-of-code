#!/usr/bin/python3

import re

ing = []
with open('input/15', 'r') as f:
    for line in f:
        m = re.search(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)
        print(m.groups())
        ing.append(m.groups())

m_1 = 0
m_2 = 0
for a in range(101):
    for b in range(0, 101-a):
        for c in range(0, 101-a-b):
            for d in range(0, 101-a-b-c):
                cap_n = 0
                dur_n = 0
                fla_n = 0
                tex_n = 0
                cal = 0
                e = (a,b,c,d)
                for f in range(4):
                    cap_n += e[f] * int(ing[f][1])
                    dur_n += e[f] * int(ing[f][2])
                    fla_n += e[f] * int(ing[f][3])
                    tex_n += e[f] * int(ing[f][4])
                    cal += e[f] * int(ing[f][5])
                if any((cap_n <= 0, dur_n <= 0, fla_n <= 0, tex_n <= 0)):
                    continue
                m_1 = max(m_1, cap_n * dur_n * fla_n * tex_n)
                if cal != 500:
                    continue
                m_2 = max(m_2, cap_n * dur_n * fla_n * tex_n)
print('Part 1: {}'.format(m_1))
print('Part 2: {}'.format(m_2))
