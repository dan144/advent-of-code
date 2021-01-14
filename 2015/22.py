#!/usr/bin/env python3

import itertools
import re
import sys

from copy import copy, deepcopy

import utils

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = float('inf')
p2 = 0

vals = []
with open(input_file) as f:
    boss_hp = int(re.search(r'\d+', f.readline()).group(0))
    boss_at = int(re.search(r'\d+', f.readline()).group(0))

class Fighter:
    def __init__(self, hp, at, mana):
        self.hp = hp
        self.at = at
        self.df = 0
        self.mana = mana

    def stats(self):
        return (self.hp, self.at, self.df, self.mana)

class Spell:
    def __init__(self, cost, turns, at, df, heal, mana):
        self.cost = cost
        self.turns = turns
        self.at = at
        self.df = df
        self.heal = heal
        self.mana = mana

    def stats(self):
        return (self.cost, self.turns, self.at, self.df, self.heal, self.mana)

missile =  Spell(53,  1, 4, 0, 0, 0)
drain =    Spell(73,  1, 2, 0, 2, 0)
shield =   Spell(113, 6, 0, 7, 0, 0)
poison =   Spell(173, 6, 0, 0, 0, 0)
recharge = Spell(229, 5, 0, 0, 0, 101)

all_spells = [
    recharge,
    shield,
    poison,
    drain,
    missile,
]

def fight(player, boss, hard_mode, cost=None, spells=None, next_spell=None):
    global lowest
    if spells is None:
        spells = {}
    if cost is None:
        cost = []

    player_go = True
    while player.hp > 0 and boss.hp > 0:
        if player_go and next_spell is None:
            # pick the next spell
            for spell in all_spells:
                if sum(cost) + spell.cost < lowest: # cheap enough to try
                    result, t_cost = fight(copy(player), copy(boss), hard_mode, cost=deepcopy(cost), spells=deepcopy(spells), next_spell=spell)
                    if result and t_cost < lowest:
                        lowest = t_cost
                        print(f' Player wins: {lowest}   \r', end='')
            return True, lowest

        if hard_mode and player_go:
            player.hp -= 1
            if player.hp <= 0:
                return False, sum(cost)

        if spells.get(173): # poison
            boss.hp -= 3
        if boss.hp <= 0:
            return True, sum(cost)

        if spells.get(229): # recharge
            player.mana += spells[229].mana

        for s_cost, spell in copy(list(spells.items())):
            spell.turns -= 1
            if spell.turns == 0:
                player.at -= spell.at
                player.df -= spell.df
                spells.pop(s_cost)

        if player_go:
            if next_spell.cost in spells.keys() and spells[next_spell.cost].turns > 0:
                return False, sum(cost)

            player.mana -= next_spell.cost
            if player.mana < 0:
                return False, sum(cost)
            cost.append(next_spell.cost)

            player.at += next_spell.at
            player.df += next_spell.df

            spells[next_spell.cost] = copy(next_spell)
            if next_spell.cost == 73:
                player.hp += 2
            next_spell = None

            boss.hp -= player.at
        else:
            player.hp -= max(1, boss.at - player.df)
        player_go = not player_go

    return player.hp > 0, sum(cost)

player_hp = 10 if test else 50
player_mana = 250 if test else 500

o_player = Fighter(player_hp, 0, player_mana)
o_boss = Fighter(boss_hp, boss_at, 0)

lowest = float('inf')
_, p1 = fight(copy(o_player), copy(o_boss), False)
print()
print(f'Part 1: {p1}')

lowest = float('inf')
_, p2 = fight(copy(o_player), copy(o_boss), True)
print()
print(f'Part 2: {p2}')
