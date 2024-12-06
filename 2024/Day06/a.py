with open('./2024/Day06/testinput.txt', 'r') as f:
    lines: str = f.read().splitlines()
    grid = [list(line) for line in lines]

import re
from collections import defaultdict

turns = defaultdict(list)
gaurds = []

for y, line in enumerate(lines):
    obstructions = re.finditer(r"#", line)
    for gaurd in re.finditer(r"\^", line):
        gaurds.append((gaurd.group(), gaurd.start(), y))
    
    for obstruction in obstructions:
        char, x, end = obstruction.group(), obstruction.start(), obstruction.end()

        # Add surrounding locations to turns
        if x < 0 or x >= len(line) or y < 0 or y >= len(grid):
            continue
        
        turns[(x, y - 1)].append((0, -1))
        turns[(x, y + 1)].append((0, 1))
        turns[(x - 1, y)].append((0, 1))
        turns[(x + 1, y)].append((0, -1))
         
print(gaurds, turns)