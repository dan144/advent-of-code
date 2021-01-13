#!/usr/bin/env python3

import itertools
import re
import sys

from copy import copy

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
        return (self.hp, self.at, self.mana)

o_boss = Fighter(boss_hp, boss_at, 0)

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

missile = Spell(53, 1, 4, 0, 0, 0)
drain = Spell(73, 1, 2, 0, 2, 0)
shield = Spell(113, 6, 0, 7, 0, 0)
poison = Spell(173, 6, 0, 0, 0, 0)
recharge = Spell(229, 5, 0, 0, 0, 101)

all_spells = [
    recharge,
    shield,
    poison,
    drain,
    missile,
]

def fight(player, boss, spellbook, hard_mode):
    player_go = 0
    spells = {}
    while player.hp > 0 and boss.hp > 0:
        if hard_mode and player_go % 2 == 0:
            # player turn, hard mode
            player.hp -= 1
            if player.hp <= 0:
                return player, boss, spellbook
        #print('Turn', player_go, 'player' if player_go % 2 == 0 else 'boss')
        #print('Player', player.hp, sum([spell.df for spell in spells.values()]), player.mana)
        #print('Boss', boss.hp)

        for spell in spells.values():
            spell.turns -= 1
            if spell.cost == 173: # poison
                boss.hp -= 3
            if spell.cost == 229: # recharge
                player.mana += spell.mana
            if boss.hp <= 0:
                return player, boss, spellbook

        if player_go % 2 == 0:
            spell = copy(spellbook.pop(0))
            if spell.cost in spells.keys():
                return player, boss, spellbook
            if spell.cost > player.mana:
                return player, boss, spellbook
            player.mana -= spell.cost
            player.at += spell.at
            player.df += spell.df

            spells[spell.cost] = copy(spell)
            if spell.cost == 73:
                player.hp += 2

            boss.hp -= player.at
        else:
            player.hp -= max(1, boss.at - player.df)
        player_go += 1

        for spell in copy(list(spells.values())):
            if spell.turns == 0:
                player.at -= spell.at
                player.df -= spell.df
                spells.pop(spell.cost)
    return player, boss, spellbook

def run(hard, n):
    ans = 1295 #float('inf')
    while ans >= 1295:
        print('Spellbooks of length', n)
        x = 0
        print(len(all_spells)**n)
        for spellbook in itertools.product(all_spells, repeat=n):
            x += 1
            print(f'\r{x}', end='')
            player = Fighter(player_hp, 0, player_mana)
            cost = sum([spell.cost for spell in spellbook])
            if cost >= ans:
                continue
            try:
                player, boss, leftovers = fight(player, copy(o_boss), list(spellbook), hard)
            except IndexError:
                pass #print('Need more spells!')
            else:
                if boss.hp <= 0:
                    print([spell.cost for spell in spellbook])
                    cost -= sum([spell.cost for spell in leftovers])
                    print('Player wins:', cost)
                    ans = min(ans, cost)
        n += 1
    return ans

player_hp = 10 if test else 50
player_mana = 250 if test else 500

p1 = run(False, 9)
print(f'Part 1: {p1}')
p2 = run(True, 12)
# below 1362 (from 10)
# below 1295 (from 11)
print(f'Part 2: {p2}')
