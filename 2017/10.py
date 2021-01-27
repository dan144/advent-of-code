#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

with open(input_file) as f:
    lengths = utils.load_comma_sep_nums(f)

nums = list(range(5 if test else 256))
n = len(nums)

def run(pos, skip):
    for l in lengths:
        if l > n:
            continue

        to_rev = (nums + nums)[pos:l+pos]

        for i, num in enumerate(to_rev[::-1]):
            nums[(pos + i) % n] = num
        assert len(nums) == n

        pos += l + skip
        pos %= n
        skip += 1
    return pos, skip

pos = 0
skip = 0
pos, skip = run(pos, skip)
p1 = nums[0] * nums[1]

print(f'Part 1: {p1}')

with open(input_file) as f:
    inp = f.readline().rstrip()
nums = list(range(5 if test else 256))
n = len(nums)

asciis = []
for c in inp:
    asciis.append(ord(c))
lengths = asciis + [17, 31, 73, 47, 23]

pos = 0
skip = 0
for _ in range(64):
    pos, skip = run(pos, skip)

hash_nums = []
for i in range(len(nums) // 16):
    v = 0
    for j in range(16):
        v ^= nums[16 * i + j]
    hash_nums.append(v)

p2 = ''
for n in hash_nums:
    v = hex(n)[2:]
    if len(v) == 1:
        v = '0' + v
    p2 += v

print(f'Part 2: {p2}')
