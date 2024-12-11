with open('./2024/Day08/input.txt', 'r') as f:
    lines: str = f.read().splitlines()
    grid = [list(line) for line in lines]

from collections import defaultdict
from itertools import combinations

nodes = defaultdict(list)
antinodes = set()

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char != ".":
            nodes[char].append((x, y))
            
print(nodes)

for node, positions in nodes.items():
    pairs = list(combinations(positions, 2))
    
    for pair in pairs:
        diff = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])
        print(pair, diff)
        antinode_1 = (pair[0][0] + diff[0], pair[0][1] + diff[1])
        antinode_2 = (pair[0][0] - 2*diff[0], pair[0][1] - 2*diff[1])
        
        if antinode_1[0] in range(len(grid[0])) and antinode_1[1] in range(len(grid)):
            antinodes.add(antinode_1)    
        
        if antinode_2[0] in range(len(grid[0])) and antinode_2[1] in range(len(grid)):
            antinodes.add(antinode_2)
            
print(antinodes, len(antinodes))