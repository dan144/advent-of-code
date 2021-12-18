#!/usr/bin/env python3

import itertools
import re
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p2 = 0

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.strip())

# Part 1
def mag(line):
    a, b = line

    if type(a) == list:
        a = mag(a)
    if type(b) == list:
        b = mag(b)
    return 3 * a + 2 * b

def add(a, b):
    val = f'[{a},{b}]'
    old = ''
    while old != val:
        level = 0
        vals = []
        f_val = 0
        start = 0

        old = val
        max_d = 0
        for i, c in enumerate(old):
            if c == '[':
                level += 1
                vals = []
                f_val = 0
                start = i
            elif c == ']':
                max_d = max(max_d, level)
                if val[i-1] in '0123456789':
                    vals.append(f_val)
                if len(vals) == 2: # found pair of numbers
                    if level > 4:
                        # explode
                        r = f'[{vals[0]},{vals[1]}]'

                        # check for number after
                        for sj in range(i, len(val)):
                            if val[sj] in '0123456789':
                                break
                        if sj < len(val) - 1:
                            sk = sj
                            while val[sk] in '0123456789':
                                sk += 1
                            second = int(val[sj:sk])
                            second += vals[1]
                            val = val[:sj] + str(second) + val[sk:]

                        # replace exploded pair
                        val = val[:start] + '0' + val[i+1:]

                        # check for number before
                        for fj in range(start-1, -1, -1):
                            if val[fj] in '0123456789':
                                break
                        if fj > 0:
                            fk = fj
                            while val[fk] in '0123456789':
                                fk -= 1
                            # number from fk+1 to fj
                            first = int(val[fk+1:fj+1])
                            first += vals[0]
                            val = val[:fk+1] + str(first) + val[fj+1:]

                        break
                level -= 1
                vals = []
                f_val = 0
            elif c in '0123456789':
                f_val *= 10
                f_val += int(c)
            elif c == ',':
                if val[i-1] in '0123456789': # was a number
                    vals.append(f_val)
                    f_val = 0

        else: # no explode, so split
            assert max_d <= 4
            nums = map(int, re.findall(r'[0-9]+', val))
            for num in nums:
                if num > 9:
                    m = re.search(r'[,\[]' + str(num) + r'[,\]]', val)
                    first = num // 2
                    second = num // 2 + (num % 2)
                    val = val[:m.start()+1] + f'[{first},{second}]' + val[m.end()-1:]
                    break
        assert eval(val)
    return val

val = None
for line in inp:
    if not val:
        val = line
    else:
        val = add(val, line)

p1 = mag(eval(val))
print(f'Part 1: {p1}')

# Part 2
for a, b in itertools.permutations(inp, 2): # slow but it works
    p2 = max(p2, mag(eval(add(a, b))))
print(f'Part 2: {p2}')
