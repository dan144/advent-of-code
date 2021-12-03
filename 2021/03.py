#!/usr/bin/env python3

import sys

import utils
### available functions:
# get_grid_edges: min_x, min_y, max_x, max_y
# display_grid
# find_dist(grid, 0, (x,y) start, (x,y) dest) - open=True, wall=False
# manh(p1[, p2]) - n-dim Manhattan dist; omit p2 for dist from origin
# is_prime

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p2 = 1

inp = []
with open(input_file) as f:
    for line in f:
        inp.append(line.strip())

# Part 1
counts = [0] * len(inp[0])

for num in inp:
    for i, bit in enumerate(num):
        # keep a count of 1s minus count of 0s for each position
        counts[i] += 1 if bit == '1' else -1

# for each value in counts, map a cast of the str value of the more common digit, then join
g = ''.join((map(lambda x: '1' if x > 0 else '0', counts)))
e = ''.join((map(lambda x: '0' if x > 0 else '1', counts)))

p1 = int(g, 2) * int(e, 2)
print(f'Part 1: {p1}')

# Part 2
for t in range(2):
    nums = set(inp) # order doesn't matter and set doesn't need an import like copy
    i = 0
    while len(nums) > 1:
        o_less_z = 0
        for num in nums:
            o_less_z += 1 if num[i] == '1' else -1

        if t == 0: # oxygen, most common
            d = '1' if o_less_z >= 0 else '0'
        else: # CO2, least common
            d = '0' if o_less_z >= 0 else '1'

        nums = set(filter(lambda x: x[i] == d, nums))
        i += 1
    p2 *= int(nums.pop(), 2) # the last num is one of the two desired values, just multiply them

print(f'Part 2: {p2}')
