with open('./2024/Day04/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

def direction_print(direction):
    lookup = {(1, -1): "↗", (1, 1): "↘", (-1, 1): "↙", (-1, -1): "↖"}
    
    return lookup[direction]

def find_starts(grid):
    starts = []
    
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == "A":
                starts.append((j, i))

    return starts

# DFS from the A to check all directions to complete the "X-MAS"
def valid_xmas(x, y, grid):
    # clockwise starting at N
    checks = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    cur_total = 0
    cur_cross = ""
    
    for check in checks:
        print(f"Checking A at {x}, {y} in direction {direction_print(check)}")
        nx, ny =  x + check[0], y + check[1]
        chars = ["M", "S"]
        
        if nx < 0 or nx == len(grid) or ny < 0 or ny == len(grid):
            break
        
        if grid[ny][nx] in chars:
            cur_cross += grid[ny][nx]
    
    if cur_cross in ["MMSS", "SSMM", "SMMS", "MSSM"]:
        cur_total += 1
        print("Found X-MAS current total:", cur_total)
            
    return cur_total
            
    # for i in range(range_start, range_end):

def calculate_total(lines):
    total = 0
    grid = [list(line) for line in lines]
    starts = find_starts(grid)

    for start in starts:
        total += valid_xmas(start[0], start[1], grid)


    return total

total = calculate_total(lines)
print(f"Total: {total}")