with open('./2024/Day04/testinput.txt', 'r') as f:
    lines: str = f.read().splitlines()

def find_starts(grid):
    starts = []
    
    for i, line in enumerate(grid):
        if "X" in line:
            starts.append((line.index("X"), i))
    
    return starts

# DFS from the X to check all directions to complete the word "XMAS"
def valid_xmas(x, y, grid):
    # clockwise
    checks = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    
    for check in checks:
        nx, ny =  x + check[0], y + check[1]
        chars = ["M", "A", "S"]
        i = 0
        total = 0
        
        while nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
            if grid[nx][ny] == chars[i]:
                nx, ny = nx + check[0], ny + check[1]
                i += 1
            
            if i == len(chars):
                total += 1
            
        return total
            
    # for i in range(range_start, range_end):

def calculate_total(lines):
    total = 0
    grid = [list(line) for line in lines]
    starts = find_starts(grid)

    for start in starts:
        total += valid_xmas(start[1], start[0], grid)


    return total

total = calculate_total(lines)
print(f"Total: {total}")