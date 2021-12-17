#!/usr/bin/env python3

import re
import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

with open(input_file) as f:
    xl, xh, yl, yh = map(int, re.findall(r'-?[0-9]+', f.readline()))

def do_step(x, y, vx, vy):
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1
    return x, y, vx, vy

# kind of hacky, just guessed at the upper bound for vy until it worked
for v_y in range(150, yl-1, -1):
    # this only works if the x range is right of 0,0
    for v_x in range(xh, 0, -1): # vx can be as high as a single movement to the far end
        vx = v_x
        vy = v_y

        max_y = 0
        x, y = 0, 0
        step = 0
        good = False
        while step < 500: # guessed at the upper bound required to ensure enough steps toward target
            step += 1
            x, y, vx, vy = do_step(x, y, vx, vy)
            max_y = max(max_y, y)
            if x in range(xl, xh+1) and y in range(yl, yh+1):
                good = True
                break # in the target zone
            if y < yl: # too low, will never make it back up
                break
            if vx > 0 and x > xh: # too far, will never make it back
                break

        if good:
            p1 = max(p1, max_y)
            p2 += 1

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
