#!/usr/bin/python3

import collections
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
players = int(inputs[0].split()[0])
marbles = int(inputs[0].split()[6])
if testing:
    print(players, marbles)

print()
print('PART ONE')
ans = 0

circle = collections.deque()
scores = [0] * players
player = -1
current = 0
for m in range(marbles + 1):
    if m % 10000 == 0:
        print(m)
    player = (player + 1) % players
    if m > 0 and m % 23 == 0:
        scores[player] += m
        remove = current - 7
        if remove > 0:
            circle.rotate(remove * -1)
            scores[player] += circle.popleft()
            current = 0
        elif remove < 0:
            circle.rotate(remove)
            scores[player] += circle.pop()
            current = 0
        else:
            scores[player] += circle.pop()
            current = 0
        #m = circle[new_current]
    else:
        if len(circle) < 2 or current + 2 == len(circle):
            circle.append(m)
            current = len(circle) - 1
        else:
            offset = 2
            current = (current + offset) % (len(circle))
            circle.rotate(current * -1)
            circle.appendleft(m)
            circle.rotate(current)
        #current = circle.index(m)
    if testing and len(circle) < 50:
        print(player, current, circle[current], circle)
#print(scores)
ans = max(scores)

print(ans)
if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')


print()
print('PART TWO')
ans = 0



print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
