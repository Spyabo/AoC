with open('./2024/Day06/testinput.txt', 'r') as f:
    lines: str = f.read().splitlines()

# Find all the locations that would form rectangles from existing path
import re
from collections import defaultdict

def find_gaurds_and_obstructions(lines):
    turns = defaultdict(list)
    gaurds = []
    
    for y, line in enumerate(lines):
        for gaurd in re.finditer(r"\^", line):
            gaurds.append((gaurd.group(), gaurd.start(), y))
            
    print(gaurds, turns)
    return gaurds, turns

def traverse(lines):
    guards, turns = find_gaurds_and_obstructions(lines)
    
    for gaurd in guards:
        direction = (0, -1)
        nx, ny = gaurd[1] + direction[0], gaurd[2] + direction[1]
        seen = set()
        seen.add((gaurd[1], gaurd[2]))
        
        while nx >= 0 and nx < len(lines[0]) and ny >= 0 and ny < len(lines)-1:
            # print(nx, ny, direction)
            
            if lines[ny + direction[1]][nx + direction[0]] == "#":
                # print("hit a wall")
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
        
        return seen

def find_parallel_lines(points):
    def calculate_slope(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            return 'vertical'
        elif y1 == y2:
            return 0
        else:
            dx = x2 - x1
            dy = y2 - y1
            gcd = abs(__import__('math').gcd(dy, dx))
            return (dy // gcd, dx // gcd)

    slope_to_lines = defaultdict(list)
    points = list(points)
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = points[i], points[j]
            slope = calculate_slope(p1, p2)
            slope_to_lines[slope].append((p1, p2))

    parallel_lines = {slope: lines for slope, lines in slope_to_lines.items() if len(lines) > 1}

    return parallel_lines

def print_line_visualisation(lines, points):
    max_x = max(x for x, y in points)
    max_y = max(y for x, y in points)
    grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y in points:
        grid[max_y - y][x] = 'O'

    for line in lines:
        for (x1, y1), (x2, y2) in line:
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    grid[max_y - y][x1] = '|'
            elif y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[max_y - y1][x] = '-'
            else:
                dx = x2 - x1
                dy = y2 - y1
                gcd = abs(__import__('math').gcd(dx, dy))
                step_x = dx // gcd
                step_y = dy // gcd
                x, y = x1, y1
                while (x, y) != (x2 + step_x, y2 + step_y):
                    grid[max_y - y][x] = '*'
                    x += step_x
                    y += step_y

    for row in grid:
        print(' '.join(row))

points = traverse(lines)
parallel_lines = find_parallel_lines(points)
for slope, lines in parallel_lines.items():
    print(f"Slope: {slope}, Lines: {lines}")
    
all_lines = [line_group for line_group in parallel_lines.values()]
print_line_visualisation(all_lines, points)