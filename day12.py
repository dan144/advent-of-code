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

# initial state: ##.#...#.#.#....###.#.#....##.#...##.##.###..#.##.###..####.#..##..#.##..#.......####.#.#..#....##.#
# #.#.# => #
board = list(inputs[0].split(': ')[1])
actions = {}
for a in inputs[2:]:
    i, o = a.split(' => ', 1)
    actions[i] = o

m = 0
val = 0
pattern = [0] * 10
generations = 50000000000
for i in range(generations):
    board = ['.']*4 + board + ['.']*4
    m += 2
    if testing:
        print(i, '\t', ''.join(board))
    old = ''.join(board[:5])
    board = board[5:]
    n = [actions.get(old, '.')]
    while board:
        old = old[1:] + board.pop(0)
        n.append(actions.get(old, '.'))
    while n[0] == '.':
        m -= 1
        n.pop(0)
    while n[-1] == '.':
        n.pop()
    board = n
    last = val
    val = sum([j - m for j in range(len(board)) if board[j] == '#'])
    pattern = pattern[1:] + [val - last]
    if i == 19:
        ans = val
        print(ans)
    if i > 20 and all([pattern[j] == pattern[j+1] for j in range(len(pattern) - 1)]):
        break

if testing:
    if part_one == ans:
        print('PART ONE CORRECT')
    else:
        print('PART ONE FAILED')

print()
print('PART TWO')

# pattern:  at generation 89, the number of plants is 5145
#           after that, each generation increases by 50

print('Generation', i, 'value:', val)
print('Generational increment:', pattern[-1])
ans = val + (generations - i - 1) * pattern[-1]

print(ans)
if testing:
    if part_two == ans:
        print('PART TWO CORRECT')
    else:
        print('PART TWO FAILED')
