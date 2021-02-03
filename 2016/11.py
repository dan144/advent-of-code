#!/usr/bin/env python3

import itertools
import re
import sys

from copy import deepcopy

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

class Item:
    def __init__(self, name):
        element, itype = name.split()
        if itype == 'microchip':
            element = element.split('-')[0]
        self.element = element
        self.itype = itype[0].upper()

    def __repr__(self):
        return ' '.join((self.element, self.itype))

    def __eq__(self, other):
        return self.element == other.element and self.itype == other.itype

    #def __str__(self):
    #    return self.element + self.itype

    def __hash__(self):
        return hash((self.element, self.itype))

floors = []
with open(input_file) as f:
    for line in f:
        floors.append([])
        for thing in re.findall(r'a ([a-z-]+ [a-z]+)', line):
            floors[-1].append(Item(thing))

def my_gen_on_floor(floor, element):
    for item in floor:
        if item.itype == 'G' and item.element == element:
            return True
    return False

def n_gen_on_floor(floor):
    n = len([item for item in floor if item.itype == 'G'])
    return n

def validate(floors):
    for floor in floors:
        for item in floor:
            if item.itype == 'M':
                if not my_gen_on_floor(floor, item.element) and n_gen_on_floor(floor) > 0:
                    return False
    return True

def tupled(floors):
    f = []
    for floor in floors:
        f.append(tuple(sorted(floor, key=lambda x: x.element + x.itype)))
    return tuple(f)

def listed(floors):
    f = []
    for floor in floors:
        f.append(list(sorted(floor, key=lambda x: x.element + x.itype)))
    return f

def move(states, steps):
    global seen

    next_states = {}
    for floors, cur_floor in states.items():
        if not floors[0] and not floors[1] and not floors[2]:
            return True, steps

        seen[(floors, cur_floor)] = steps
        floors = listed(floors)

        floor = floors[cur_floor]
        for m in [1, -1]:
            next_floor = cur_floor + m
            if next_floor < 0 or next_floor > 3:
                continue

            for f, s in itertools.combinations_with_replacement(floors[cur_floor], 2):
                next_floors = deepcopy(floors)
                f, s = sorted((f, s), key=lambda x: x.element + x.itype, reverse=True)

                next_floors[cur_floor].remove(f)
                next_floors[next_floor].append(f)
                if s != f:
                    next_floors[cur_floor].remove(s)
                    next_floors[next_floor].append(s)

                if not validate(next_floors):
                    continue

                t = tupled(next_floors)
                check = seen.get((t, next_floor), float('inf'))
                if check < steps:
                    continue

                next_states[t] = next_floor

    if next_states:
        return move(deepcopy(next_states), steps + 1)
    return True, steps

seen = {}
done, p1 = move({tupled(floors): 0}, 0)
assert done
print(f'\nPart 1: {p1}')

seen = {}
for n in ['elerium generator', 'elerium-compatible microchip', 'dilithium generator', 'dilithium-compatible microchip']:
    floors[0].append(Item(n))
done, p2 = move({tupled(floors): 0}, 0)
assert done
print(f'\nPart 2: {p2}')
