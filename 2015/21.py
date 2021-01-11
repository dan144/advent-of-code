#!/usr/bin/env python3

import itertools
import re
import sys

from copy import deepcopy

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = float('inf')
p2 = 0

vals = []
with open(input_file) as f:
    for line in f:
        vals.append(int(re.search(r'\d+', line).group(0)))

class Fighter:
    def __init__(self, hp, at, df):
        self.hp = hp
        self.at = at
        self.df = df

    def stats(self):
        return (self.hp, self.at, self.df)

def fight(player, boss):
    player_go = True
    while player.hp > 0 and boss.hp > 0:
        if player_go:
            boss.hp -= max(1, player.at - boss.df)
        else:
            player.hp -= max(1, boss.at - player.df)
        player_go = not player_go
    return player, boss

o_boss = Fighter(*vals)

weapons = {
    8: (4, 0),
    10: (5, 0),
    25: (6, 0),
    40: (7, 0),
    74: (8, 0),
}

armors = {
    0: (0, 0), # armor is optional
    13: (0, 1),
    31: (0, 2),
    53: (0, 3),
    75: (0, 4),
    102: (0, 5),
}

all_rings = {
    25: (1, 0),
    50: (2, 0),
    100: (3, 0),
    20: (0, 1),
    40: (0, 2),
    80: (0, 3),
}

for weapon in weapons.items():
    for armor in armors.items():
        for n_rings in range(3): # 0-2 rings can be used
            for rings in itertools.combinations(all_rings.items(), n_rings):
                cost = weapon[0] + armor[0] + sum([ring[0] for ring in rings])
                at = weapon[1][0] + armor[1][0] + sum([ring[1][0] for ring in rings])
                df = weapon[1][1] + armor[1][1] + sum([ring[1][1] for ring in rings])

                player_hp = 8 if test else 100
                player_at = 5 if test else at
                player_df = 5 if test else df

                player = Fighter(player_hp, player_at, player_df)
                player, boss = fight(player, deepcopy(o_boss))
                if player.hp > 0:
                    p1 = min(p1, cost)
                else:
                    p2 = max(p2, cost)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
