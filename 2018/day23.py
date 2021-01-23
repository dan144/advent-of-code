#!/usr/bin/python3

import json
import sys

import utils

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

drones = set()
maxd = None
max_radius = 0
mins = [None] * 3
maxs = [None] * 3
for line in inputs:
    p = line.split(', ')
    x, y, z = list(map(int, p[0].split('<')[1][:-1].split(',')))
    r = int(p[1].split('=')[1])
    drone = (x, y, z, r)
    drones.add(drone)
    if mins[0] is None or x < mins[0]:
        mins[0] = x
    if mins[1] is None or y < mins[1]:
        mins[1] = y
    if mins[2] is None or z < mins[2]:
        mins[2] = z
    if maxs[0] is None or x > maxs[0]:
        maxs[0] = x
    if maxs[1] is None or y > maxs[1]:
        maxs[1] = y
    if maxs[2] is None or z > maxs[2]:
        maxs[2] = z
    if maxd is None or r > maxd[3]:
        maxd = drone

max_radius = maxd[3]

ans = 0
for drone in drones:
    if utils.manh(drone[:3], maxd[:3]) <= max_radius:
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

def parse(spots):
    #print(spots)
    most_in_range = 0
    closest = None
    for spot in spots:
        in_range = 0
        for drone in drones:
            #print(spot, drone)
            in_range += 1 if utils.manh(spot, drone[:3]) <= drone[3] else 0
        if in_range > most_in_range:
            most_in_range = in_range
            closest = spot
    return most_in_range, closest


most_in_range = 0
most_dist = None

print(mins, maxs)

# FAILS
# 0
# 99699201 - too high

# most drones seen: 745
# lowest dist: 51115112

xa, ya, za = 0, 0, 0
for drone in drones:
    xa += drone[0]
    ya += drone[1]
    za += drone[2]
xa /= len(drones)
ya /= len(drones)
za /= len(drones)
xa -= 3000000
ya -= 3000000
za -= 3000000
print(xa, ya, za)

spots = {(int((maxs[0] + mins[0])/5) - 300000, int((maxs[1] + mins[1])/5), int((maxs[2] + mins[2])/5))}
#spots = {(max(mins[0], 0), max(mins[1], 0), max(mins[2], 0))}
#spots = {(int(xa), int(ya), int(za))}
spots = {(0,0,0)}
spots = set()
for drone in drones:
    spots.add((drone[0], drone[1], drone[2]))
spots = {tuple(map(int, '22589400,27970303,28128013'.split(',')))}
inc = 1
print(spots)
seen = set()
#most_dist = 602183102
most_dist = 78687716
while spots:
    in_range, closest = parse(spots)
    if closest:
        m_dist = utils.manh(closest)
        #print(len(spots), m_dist)
        if in_range > most_in_range or (in_range == most_in_range and m_dist < most_dist):
            most_in_range = in_range
            most_dist = m_dist
            print('At {} (Manhattan distance {}) there are {} drones in range'.format(','.join(map(str, closest)), most_dist, in_range))

    n = set()
    seen.update(spots)
    spots = {closest}
    for x, y, z in spots:
        for dx, dy, dz in {(-1*inc, 0, 0), (1*inc, 0, 0), (0, -1*inc, 0), (0, 1*inc, 0), (0, 0, -1*inc), (0, 0, 1*inc)}:
            if x+dx < mins[0] or x+dx > maxs[0]:
                continue
            if y+dy < mins[1] or y+dy > maxs[1]:
                continue
            if z+dz < mins[2] or z+dz > maxs[2]:
                continue
            to_add = (x+dx, y+dy, z+dz)
            if to_add not in seen and utils.manh(to_add) < most_dist:
                n.add(to_add)
    spots = n

ans = most_dist
print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
