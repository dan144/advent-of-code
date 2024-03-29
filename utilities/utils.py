# utility functions for advent of code

import math

### load functions
def load_grid(f, cast_to=str):
    # returns a dict with (x,y) -> <char> values
    lines = []
    for line in f:
        lines.append(line)
    return parse_grid(lines, cast_to)

def load_num_lines(f):
    nums = []
    for line in f:
        nums.append(int(line.rstrip()))
    return nums

def load_one_line_of_nums(f):
    return list(map(int, f.readline().rstrip().split()))

def load_comma_sep_nums(f):
    return list(map(int, f.readline().rstrip().split(',')))

def load_split_lines(f):
    inp = []
    for line in f:
        inp.append(line.rstrip().split())
    return inp

### util functions

# graph functions
def get_grid_edges(grid):
    mnx = min({x for x, y in grid.keys()})
    mny = min({y for x, y in grid.keys()})
    mxx = max({x for x, y in grid.keys()})
    mxy = max({y for x, y in grid.keys()})
    return mnx, mny, mxx, mxy

def display_grid(grid, d=' '):
    mnx, mny, mxx, mxy = get_grid_edges(grid)

    for x in range(mnx, mxx + 1):
        for y in range(mny, mxy + 1):
            print(grid.get((x, y), d), end='')
        print()

def parse_grid(lines, cast_to=str):
    grid = {}
    for x, line in enumerate(lines):
        for y, c in enumerate(line.rstrip()):
            grid[x, y] = cast_to(c)
    return grid

adjs = {(-1, 0), (1, 0), (0, -1), (0, 1)}
diags = {(-1, -1), (-1, 1), (1, -1), (1, 1)}
all_dirs = adjs | diags

def find_dist(grid, dist, locs, dest):
    # recursively find distance (initially 0) from locs (initially source) to dest
    # locs is set(x,y tuple), dest is x,y tuple
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

def find_cheapest(grid, start, end):
    locs = {start}
    costs = {start: 0}

    while locs: # search until no change in grid
        n_locs = set()
        for y, x in locs:
            for dx, dy in adjs:
                nx = x + dx
                ny = y + dy
                if (ny, nx) not in grid:
                    continue
                cost = costs.get((y, x), float('inf')) + grid[ny, nx]
                if cost <= costs.get((ny, nx), float('inf')):
                    # if cheaper this way, update cost and reconsider this point
                    costs[ny, nx] = cost
                    n_locs.add((ny, nx))
        locs = n_locs

    return costs

def transpose_grid(grid):
    n_grid = {}
    for (x, y), v in grid.items():
        n_grid[y, x] = v
    return n_grid

def manh(p1, p2=None):
    # n-dim Manhattan distance
    assert p2 is None or len(p1) == len(p2)
    d = 0
    for i in range(len(p1)):
        a = p1[i]
        b = p2[i] if p2 else 0
        d += abs(a - b)
    return d

def is_prime(n):
    for factor in range(2, int(math.sqrt(n)) + 1):
        if (n / factor) % 1 == 0:
            return False
    return True
