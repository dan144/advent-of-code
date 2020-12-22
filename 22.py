#!/usr/bin/env python3

import re
import sys

from copy import copy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0
p2 = 0

deck1 = []
deck2 = []
in_p2 = False
with open(input_file) as f:
    for line in f:
        try:
            card = int(line[:-1])
            if in_p2:
                deck2.append(card)
            else:
                deck1.append(card)
        except:
            if line == '\n':
                in_p2 = True
            pass
odeck1 = copy(deck1)
odeck2 = copy(deck2)

while deck1 and deck2:
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    if card1 > card2:
        deck1 += [card1, card2]
    else:
        deck2 += [card2, card1]

deck = deck1 + deck2
x = len(deck)
for i in range(1, x+1):
    p1 += deck[::-1][i-1] * i
print(f'Part 1: {p1}')

def check(deck, prev):
    d = tuple(deck)
    if d in prev:
        return True
    prev.add(copy(d))
    return False

def recurse(deck1, deck2):
    done = False
    prevs1 = set()
    prevs2 = set()
    while not done:
        if check(deck1, prevs1) or check(deck2, prevs2):
            return 1

        if len(deck1) == 0:
            return 2
        if len(deck2) == 0:
            return 1

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if len(deck1) < card1 or len(deck2) < card2:
            if card1 > card2:
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]
        else:
            w = recurse(copy(deck1[:card1]), copy(deck2[:card2]))
            if w == 1:
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]
    return w


deck1 = odeck1
deck2 = odeck2
while deck1 and deck2:
    recurse(deck1, deck2)

deck = deck1 + deck2
x = len(deck)
for i in range(1, x+1):
    p2 += deck[::-1][i-1] * i
print(f'Part 2: {p2}')
