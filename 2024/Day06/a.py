with open('./2024/Day06/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

import re
from collections import defaultdict

def find_gaurds_and_obstructions(lines):
    turns = defaultdict(list)
    gaurds = []
    
    for y, line in enumerate(lines):
        for gaurd in re.finditer(r"\^", line):
            gaurds.append((gaurd.group(), gaurd.start(), y))
        
        # obstructions = re.finditer(r"#", line)
        
        # for obstruction in obstructions:
        #     char, x, end = obstruction.group(), obstruction.start(), obstruction.end()

        #     if x < 0 or x >= len(line) or y < 0 or y >= len(lines):
        #         continue
            
        #     # Add surrounding locations to turns with new direction
        #     turns[(x, y - 1)].append((0, -1))
        #     turns[(x, y + 1)].append((0, 1))
        #     turns[(x - 1, y)].append((0, 1))
        #     turns[(x + 1, y)].append((0, -1))
            
    print(gaurds, turns)
    return gaurds, turns

def traverse(lines):
    guards, turns = find_gaurds_and_obstructions(lines)
    
    for gaurd in guards:
        direction = (0, -1)
        nx, ny = gaurd[1] + direction[0], gaurd[2] + direction[1]
        seen = set((gaurd[1], gaurd[2]))
        
        while nx >= 0 and nx < len(lines[0]) and ny >= 0 and ny < len(lines)-1:
            print(nx, ny, direction)
            
            if lines[ny + direction[1]][nx + direction[0]] == "#":
                print("hit a wall")
                match direction:
                    case (0, -1):
                        direction = (1, 0)
                    case (1, 0):
                        direction = (0, 1)
                    case (0, 1):
                        direction = (-1, 0)
                    case (-1, 0):
                        direction = (0, -1)
            
            nx, ny = nx + direction[0], ny + direction[1]
            seen.add((nx, ny))
        
        print(len(seen) - 1)
traverse(lines)