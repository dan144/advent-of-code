#!/usr/bin/env python3

import re
import sys

from collections import defaultdict

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0

allergens = {}
ingredients = defaultdict(int)
with open(input_file) as f:
    for line in f:
        data = re.search(r'([a-z ]+) \(contains ([a-z, ]+)\)', line)
        i_ingredients = data.group(1).split()
        for allergen in data.group(2).split(', '):
            if allergen not in allergens:
                allergens[allergen] = set(i_ingredients)
            else:
                allergens[allergen] &= set(i_ingredients)

        for ingredient in i_ingredients:
            ingredients[ingredient] += 1

done = False
while not done:
    done = True
    for allergen, combined in allergens.items():
        if isinstance(combined, set) and len(combined) == 1:
            food = combined.pop()
            allergens[allergen] = food
            for allergen in set(allergens.keys()) - {allergen}:
                if isinstance(allergens[allergen], set) and food in allergens[allergen]:
                    allergens[allergen].remove(food)
            done = False # reduced, run again

p1 = sum(ingredients[ingredient] for ingredient in set(ingredients.keys()) - set(allergens.values()))
print(f'Part 1: {p1}')
p2 = ','.join(ingredient for _, ingredient in sorted(allergens.items(), key=lambda x: x[0]))
print(f'Part 2: {p2}')
