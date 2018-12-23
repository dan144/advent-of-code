#!/usr/bin/python3

import json
import sys

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
    for line in f:
        inputs.append(data_type(line[:-1]))
if testing:
    print(inputs)

print()
print('PART ONE')
ans = None

drones = []
maxr = 0
for line in inputs:
    p = line.split(', ')
    x, y, z = list(map(int, p[0].split('<')[1][:-1].split(',')))
    r = int(p[1].split('=')[1])
    drones.append((x, y, z, r))
    if r > drones[maxr][3]:
        maxr = len(drones) - 1

max_radius = drones[maxr][3]

def man_dist(drone_a, drone_b):
    d = 0
    for i in range(3):
        d += abs(drone_a[i] - drone_b[i])
    return d

ans = 0
for drone in drones:
    if man_dist(drone, drones[maxr]) <= drones[maxr][3]:
        ans += 1

print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')


print()
print('PART TWO')
ans = None



print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
