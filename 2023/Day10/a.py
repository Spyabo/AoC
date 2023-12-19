with open("./2023/Day10/testinput.txt", "r") as f:
    lines: str = f.read().splitlines()
# 4687
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.

def find_s(grid):
    for i, line in enumerate(grid):
        if "S" in line:
            return line.index("S"), i


def find_starts(grid, x, y):
    starts = []

    for i, direction in enumerate([[0, 1], [1, 0], [0, -1], [-1, 0]]):
        nx, ny = x + direction[0], y + direction[1]
        
        if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
            continue
        
        if i == 0 and grid[ny][nx] in ["|", "7", "F"]:
            starts.append((nx, ny, grid[ny][nx]))
        if i == 1 and grid[ny][nx] in ["-", "J", "7"]:
            starts.append((nx, ny, grid[ny][nx]))
        if i == 2 and grid[ny][nx] in ["|", "L", "J"]:
            starts.append((nx, ny, grid[ny][nx]))
        if i == 3 and grid[ny][nx] in ["-", "L", "F"]:
            starts.append((nx, ny, grid[ny][nx]))
    
    return starts

def move(grid, x, y, direction, pipe):

    
def main():
    grid = [list(line) for line in lines]
    x, y = find_s(grid)

    while 
        

main()
