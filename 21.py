#!/usr/bin/env python3

import re
import sys

test = len(sys.argv) > 1
input_file = 'input' + sys.argv[0].split('.')[1].lstrip('/') + ('.test' if test else '')

p1 = 0

allergens = {}
all_allergens = set()
ingredients = {}
with open(input_file) as f:
    for line in f:
        data = re.search(r'([a-z ]+) \(contains ([a-z, ]+)\)', line)
        i_ingredients = data.group(1).split()
        i_allergens = data.group(2).split(', ')
        for allergen in i_allergens:
            if allergen not in allergens:
                allergens[allergen] = []
            allergens[allergen].append(set(i_ingredients))
        for ingredient in i_ingredients:
            if ingredient not in ingredients:
                ingredients[ingredient] = 0
            ingredients[ingredient] += 1
        all_allergens |= set(i_allergens)
print('All allergens:', all_allergens)
n_allergens = len(all_allergens)

mapping = {}
for allergen, allergen_list in allergens.items():
    combined = allergen_list[0]
    for l in allergen_list[1:]:
        combined &= l
    print(allergen, combined)
    mapping[allergen] = combined

done = False
while not done:
    done = True
    for allergen, combined in mapping.items():
        if isinstance(combined, set) and len(combined) == 1:
            done = False
            food = combined.pop()
            mapping[allergen] = food
            for allergen in all_allergens - {allergen}:
                if food in mapping[allergen]:
                    mapping[allergen].remove(food)

for ingredient in set(ingredients.keys()) - set(mapping.values()):
    p1 += ingredients[ingredient]
print(f'Part 1: {p1}')

p2 = ','.join(ingredient for allergen, ingredient in sorted(mapping.items(), key=lambda x: x[0]))
print(f'Part 2: {p2}')
