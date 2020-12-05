print(f'Part 1: {max(ids := {int("".join(("0" if c in "FL" else "1" for c in line[:-1])), 2) for line in open("input5", "r")})}\nPart 2: {(set(range(min(ids), max(ids) + 1)) - ids).pop()}')
