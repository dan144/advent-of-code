#!/usr/bin/env python3

import itertools
import math
import numpy
import re
import sys

import utils
# manh(p1[, p2]) - n-dim Manhattan dist; omit p2 for dist from origin

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

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
    return numpy.matrix([[ math.cos(theta), -math.sin(theta), 0],
                         [ math.sin(theta), math.cos(theta) , 0],
                         [ 0              , 0               , 1]])
# end borrowed section

all_beacons = set(scanners.pop(0))

def sumt(t1, t2):
    return tuple(map(sum, zip(t1, t2)))

def difft(t1, t2):
    v = []
    for a, b in zip(t1, t2):
        v.append(a - b)
    return tuple(v)

dirs = (0, numpy.pi/2, numpy.pi, numpy.pi/2*3)
scanner_locs = []
while scanners:
    matched = set()
    for n, beacons in scanners.items():
        is_match = False
        print(f'\rlooking at {n}', end='')
        for x in dirs:
            for y in dirs:
                for z in dirs[:2]: # removes 2 orientations that are always duplicates
                    rot = Rx(x) * Ry(y) * Rz(z)
                    rot_beacons = []
                    for beacon in beacons:
                        opos = numpy.matrix(beacon)
                        pos = opos * rot
                        rot_beacon = tuple(map(lambda i: int(round(i, 0)), pos.tolist()[0]))
                        rot_beacons.append(rot_beacon)

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
            scanner_locs.append(scanner_loc)
            for beacon in rot_beacons:
                true_beacon = sumt(scanner_loc, beacon)
                all_beacons.add(true_beacon)
            matched.add(n)
    for n in matched:
        scanners.pop(n)
    print('\rOriented', len(all_beacons), 'beacons;', len(scanners), 'remaining scanners')

p1 = len(all_beacons)
print(f'Part 1: {p1}')

# Part 2

for a, b in itertools.combinations(scanner_locs, 2):
    p2 = max(p2, utils.manh(a, b))
print(f'Part 2: {p2}')
