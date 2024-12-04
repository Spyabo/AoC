with open('./2024/Day04/testinput.txt', 'r') as f:
    lines: str = f.read().splitlines()

def direction_print(direction):
    lookup = {(0, -1): "↑",(1, -1): "↗",(1, 0): "→",(1, 1): "↘",(0, 1): "↓",(-1, 1): "↙",(-1, 0): "←",(-1, -1): "↖",}
    
    return lookup[direction]

def find_starts(grid):
    starts = []
    
    for i, line in enumerate(grid):
        if "X" in line:
            starts.append((line.index("X"), i))
    
    return starts

# DFS from the X to check all directions to complete the word "XMAS"
def valid_xmas(x, y, grid):
    # clockwise starting at N
    checks = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    cur_total = 0
    
    for check in checks:
        print(f"Checking X at {x}, {y} in direction {direction_print(check)}")
        nx, ny =  x + check[0], y + check[1]
        chars = ["M", "A", "S"]
        i = 0
        
        while True:
            if nx < 0 or nx == len(grid) or ny < 0 or ny >= len(grid):
                break
            
            if grid[ny][nx] == chars[i]:
                print("Found", chars[i], "at", nx, ny)
                nx, ny = nx + check[0], ny + check[1]
                i += 1
            else:
                nx, ny = nx + check[0], ny + check[1]
                continue
            
            if i == len(chars):
                cur_total += 1
                print("Found XMAS current total:", cur_total)
                break
            
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