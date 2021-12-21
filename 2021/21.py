#!/usr/bin/env python3

import sys

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

pos = []
with open(input_file) as f:
    for line in f:
        n = int(line.strip().split()[-1])
        pos.append(n)

# For part 2, need initial positions
# (p1 position, p2 position, p1 score, p2 score, is p2's turn?): num games
games = {
    tuple(pos) + (0, 0, False): 1,
}

# Part 1
scores = [0] * len(pos)
rolls = 0
while all(x < 1000 for x in scores):
    for player in range(len(pos)):
        for roll in range(3):
            rolls += 1
            r_v = (rolls - 1) % 100 + 1
            pos[player] += r_v
        pos[player] = (pos[player] - 1) % 10 + 1
        scores[player] += pos[player]
        if scores[player] >= 1000:
            break

p1 = rolls * sorted(scores)[0]
print(f'Part 1: {p1}')

# Part 2
wins = {
    1: 0,
    2: 0
}

# freq distribution for splitting the universe based on 3 roles {1,2,3}
dist = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}

while games:
    new = {}
    for (p1p, p2p, p1s, p2s, turn), c in games.items():
        for dp, n in dist.items(): # compute the new universes for each possible roll combo, n of each
            p = p2p if turn else p1p
            p = (p + dp - 1) % 10 + 1

            if turn:
                s = p2s + p # score increase based on position
                if s >= 21:
                    wins[2] += c * n # this combo lead to c*n wins
                else:
                    k = (p1p, p, p1s, s, False) # new state key
                    if k not in new:
                        new[k] = 0
                    new[k] += c * n # there's now n times as many of this state
            else:
                s = p1s + p
                if s >= 21:
                    wins[1] += c * n
                else:
                    k = (p, p2p, s, p2s, True)
                    if k not in new:
                        new[k] = 0
                    new[k] += c * n
    games = new

p2 = sorted(wins.values())[1]
print(f'Part 2: {p2}')
