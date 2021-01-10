# utility functions for advent of code

### load functions
def load_grid(f):
    grid = {}
    for x, line in enumerate(f.readlines()):
        for y, c in enumerate(line.rstrip()):
            grid[x, y] = c
    return grid

def load_num_lines(f):
    nums = []
    for line in f:
        nums.append(int(line.rstrip()))
    return nums

### util functions
adjs = {(-1, 0), (1, 0), (0, -1), (0, 1)}

def find_dist(grid, dist, locs, dest):
    # grid: open=True, wall=False
    new_froms = set()
    for x, y in locs:
        for dx, dy in adjs:
            nx, ny = x + dx, y + dy
            if (nx, ny) == dest:
                return dist + 1
            if grid.get((nx, ny)):
                new_froms.add((nx, ny))
    if new_froms:
        return find_dist(grid, dist + 1, new_froms, dest)
    return -1
