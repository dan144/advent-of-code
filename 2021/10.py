#!/usr/bin/env python3

import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.strip())

# Part 1
scores = []
for line in inp:
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(c)
        elif c in ')]}>':
            if stack.pop() + c not in {'()', '[]', '{}', '<>'}:
                # most recent value and current char are not valid pair
                p1 += {
                    ')': 3,
                    ']': 57,
                    '}': 1197,
                    '>': 25137,
                }[c]
                break # don't finish if found corrupt
    else:
        # can only reach if incomplete
        score = 0
        for c in stack[::-1]:
            score *= 5
            score += {
                '(': 1,
                '[': 2,
                '{': 3,
                '<': 4,
            }[c]
        scores.append(score)

print(f'Part 1: {p1}')

# Part 2
l = len(scores) // 2
p2 = sorted(scores)[l]
print(f'Part 2: {p2}')
