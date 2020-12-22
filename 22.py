#!/usr/bin/env python3

import sys

from copy import copy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

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
        except ValueError:
            if line == '\n':
                in_p2 = True
og_decks = (copy(deck1), copy(deck2))

while deck1 and deck2:
    card1 = deck1.pop(0)
    card2 = deck2.pop(0)
    if card1 > card2:
        deck1 += [card1, card2]
    else:
        deck2 += [card2, card1]

def score(deck1, deck2):
    deck = deck1 + deck2
    score = 0
    for i in range(len(deck)):
        score += deck[::-1][i] * (i + 1)
    return score

p1 = score(deck1, deck2)
print(f'Part 1: {p1}')

def check_repeat(deck, prev):
    d = tuple(deck)
    if d in prev:
        return True
    prev.add(d)
    return False

def recurse(deck1, deck2):
    prevs1 = set()
    prevs2 = set()
    while True:
        if check_repeat(deck1, prevs1) or check_repeat(deck2, prevs2):
            return 1
        if len(deck1) == 0:
            return 2
        if len(deck2) == 0:
            return 1

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if len(deck1) < card1 or len(deck2) < card2:
            # not able to recurse: simple resolution
            if card1 > card2:
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]
        else:
            winner = recurse(copy(deck1[:card1]), copy(deck2[:card2]))
            if winner == 1:
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]

deck1, deck2 = og_decks # reset the decks
recurse(deck1, deck2)
p2 = score(deck1, deck2)
print(f'Part 2: {p2}')
