#!/usr/bin/env python3

import itertools
import math
import numpy
import re
import sys

import utils
### available functions:
# manh(p1[, p2]) - n-dim Manhattan dist; omit p2 for dist from origin

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

scanners = {}
with open(input_file) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        m = re.match(r'--- scanner ([0-9]+) ---', line)
        if m:
            scanner = int(m.groups()[0])
            scanners[scanner] = []
        else:
            x, y, z = map(int, line.split(','))
            scanners[scanner].append((x, y, z))

#print(scanners)
# Part 1

# Taken from https://www.meccanismocomplesso.org/en/3d-rotations-and-euler-angles-in-python/
def Rx(theta):
    return numpy.matrix([[ 1, 0              , 0              ],
                         [ 0, math.cos(theta),-math.sin(theta)],
                         [ 0, math.sin(theta), math.cos(theta)]])

def Ry(theta):
    return numpy.matrix([[ math.cos(theta), 0, math.sin(theta)],
                         [ 0           , 1, 0                 ],
                         [-math.sin(theta), 0, math.cos(theta)]])

def Rz(theta):
    return numpy.matrix([[ math.cos(theta), -math.sin(theta), 0 ],
                         [ math.sin(theta), math.cos(theta) , 0 ],
                         [ 0              , 0               , 1 ]])

all_beacons = set(scanners.pop(0))

def sumt(t1, t2):
    return tuple(map(sum, zip(t1, t2)))

def difft(t1, t2):
    v = []
    for a, b in zip(t1, t2):
        v.append(a - b)
    return tuple(v)

dirs = (0, numpy.pi/2, numpy.pi, numpy.pi/2*3)
while scanners:
    break
    matched = set()
    print('\rOriented', len(all_beacons), 'beacons;', len(scanners), 'remaining scanners')
    for n, beacons in scanners.items():
        is_match = False
        print(f'\rlooking at {n}', end='')
        for x in dirs:
            for y in dirs:
                for z in dirs:
                    rot = Rx(x) * Ry(y) * Rz(z)
                    rot_beacons = []
                    for beacon in beacons:
                        opos = numpy.matrix(beacon)
                        pos = opos * rot
                        rot_beacon = list(map(lambda i: int(round(i, 0)), pos.tolist()[0]))
                        rot_beacons.append(tuple(rot_beacon))

                    for base_beacon in rot_beacons: # try each (rotated) beacon the scanner sees
                        for assumed_match in all_beacons: # against every known beacon
                            # (0,0,0) + assumed_match == scanner_loc + rotated beacon
                            # scanner_loc = assumed_match - beacon
                            # use this to find the potential scanner location
                            scanner_loc = difft(assumed_match, base_beacon)

                            matches = 0
                            for beacon in rot_beacons: # for all rotated beacons
                                true_beacon = sumt(scanner_loc, beacon) # compute the beacon's alleged true loc
                                if true_beacon in all_beacons: # check if it's a match to a known beacon
                                    matches += 1
                            if matches >= 12: # if 12+ matches found from this loc, it's real
                                is_match = True
                                break
                        if is_match:
                            break
                    if is_match:
                        break
                if is_match:
                    break
            if is_match:
                break

        if is_match:
            print(f'\r{n} is oriented at {scanner_loc}')
            for beacon in rot_beacons:
                true_beacon = sumt(scanner_loc, beacon)
                all_beacons.add(true_beacon)
            matched.add(n)
    for n in matched:
        scanners.pop(n)

p1 = len(all_beacons)
print(f'Part 1: {p1}')

# Part 2
# hardcoded for my input
scanner_locs = [
    (-80, 52, 1283),
    (-76, 151, -1118),
    (5, 63, 2538),
    (1240, 55, 2565),
    (1198, 151, 3697),
    (1079, 77, 4802),
    (-1179, 41, 2595),
    (-14, 1212, 2404),
    (2362, 115, 3694),
    (2377, 1258, 3717),
    (1195, 1342, 3702),
    (2426, 1273, 2530),
    (1186, 1281, 2430),
    (-59, 80, 4993),
    (2321, 2402, 3597),
    (2324, 125, 2555),
    (2452, 2497, 2417),
    (2415, 1217, 4925),
    (3544, 1368, 3737),
    (1258, 2529, 2454),
    (3551, 2397, 2409),
    (2290, 3618, 2570),
    (2438, 3714, 1365),
    (1233, 3689, 1388),
    (2364, 1239, 6023),
    (2398, 2456, 6145),
    (2358, 73, 6180),
    (3603, -11, 6028),
    (2364, 1345, 7273),
    (2406, 2571, 7337),
    (2336, 1349, 8413),
    (2386, 1183, 9749),
    (2312, 2549, 9777),
    (2329, 2553, 10906),
    (3545, 2415, 10970),
    (4729, 2504, 10854),
]

for a, b in itertools.combinations(locs, 2):
    p2 = max(p2, utils.manh(a, b))
print(f'Part 2: {p2}')
