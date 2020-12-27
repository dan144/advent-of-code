#!/usr/bin/python3

import json
import sys
from copy import copy

print('Running:',sys.argv[0])

testing = len(sys.argv) == 2

n = sys.argv[0][2:].index('.')
filen = sys.argv[0][5:n+1+len(str(n))]
input_file = 'input' + str(filen)

if testing:
    print('TESTING')
    input_file = 'test' + input_file

print('Reading:', input_file)

inputs = []
data_type = str
with open(input_file, 'r') as f:
    if testing:
        test_vals = json.loads(f.readline())
        part_one = test_vals['part_one']
        part_two = test_vals['part_two']
    inputs = list(map(int, f.readline().split()))
if testing:
    print(inputs)

print()
print('PART ONE')
ans = 0

nums = copy(inputs)

def parse_child():
    global ans
    global nums
    global vals
    global child_n
    children = nums.pop(0)
    metadata = nums.pop(0)
    my_n = child_n
    child_n += 1
    vals.append({"metadatas": [], "children": []})
    for i in range(children):
        vals[my_n]['children'].append(parse_child())
    for i in range(metadata):
        m = nums.pop(0)
        vals[my_n]['metadatas'].append(m)
        ans += m
    if children == 0:
        vals[my_n]['sum'] = sum(vals[my_n]['metadatas'])

    return my_n

child_n = 0
vals = []
parse_child()

print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')


print()
print('PART TWO')
ans = 0
vals = []
child_n = 0

def get_sum(n):
    global vals
    if 'sum' in vals[n]:
        return vals[n]['sum']

    s = 0
    for child in vals[n]['metadatas']:
        if child > 0 and child <= len(vals[n]['children']):
            c_val = vals[n]['children'][child-1]
            s += get_sum(c_val)
    vals[n]['sum'] = s
    return s

nums = copy(inputs)
parse_child()
get_sum(0)
ans = vals[0]['sum']

print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
