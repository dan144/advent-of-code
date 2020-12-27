print(max(ids := {int("".join(("0" if c in "FL" else "1" for c in line[:-1])), 2) for line in open("input05")}), (set(range(min(ids), max(ids))) - ids).pop())
