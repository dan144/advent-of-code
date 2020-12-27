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

# position=< 52672,  52690> velocity=<-5, -5>
points = []
for line in inputs:
    p, v = line.split('>', 1)
    x = int(p[p.index('<')+1:p.index(',')].strip())
    y = int(p[p.index(',')+1:].strip())
    vx = int(v[v.index('<')+1:v.index(',')].strip())
    vy = int(v[v.index(',')+1:-1].strip())
    points.append((x,y,vx,vy))

print()
print('PART ONE')
ans = None

t = 0
lastx = None
lasty = None
onboard = []
edges = None
while not ans:
    x = 0
    y = 0
    minx = None
    miny = None
    maxx = None
    maxy = None
    dots = []
    for point in points:
        mx = point[0] + (t * point[2])
        my = point[1] + (t * point[3])
        if minx is None or mx < minx:
            minx = mx
        if miny is None or my < miny:
            miny = my
        if maxx is None or mx > maxx:
            maxx = mx
        if maxy is None or my > maxy:
            maxy = my
        dots.append((mx,my))
    sizex = maxx - minx
    sizey = maxy - miny
    if not lastx or not lasty or sizex < lastx or sizey < lasty:
        lastx = sizex
        lasty = sizey
        edges = (minx, maxx, miny, maxy)
        onboard = dots
    else:
        break
    t += 1

t -= 1
board = []
minx, maxx, miny, maxy = edges
for i in range(maxy - miny + 1):
    board.append(['.'] * (maxx - minx + 1))
for mx, my in onboard:
    mx -= minx
    my -= miny
    board[my][mx] = '#'
for row in board:
    print(''.join(row))

print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')

print()
print('PART TWO')
ans = t

print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
