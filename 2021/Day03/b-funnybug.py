with open('./2021/Day03/testinput.txt', 'r') as f:
    lines: str = f.read().splitlines()

def solve(lines, bool):
    grid = [[] for x in range(len(lines[0]))]

    for line in lines:
        for i, c in enumerate(line):
            grid[i].append(c)
        
    for pos in grid:
        keep = max(set(pos), key=pos.count) if bool else min(set(pos), key=pos.count)
        new_pos = []
        for i, bit in enumerate(pos):
            if bit == keep:
                new_pos.append(bit)
            else:
                for pos in grid:
                    pos.pop(i)

    ans = ""

    for res in grid:
        if len(res) == 2:
            if "1" in res:
                take = res.index("1")
            ans += res[take]
        else:
            ans += res[0]
        
        print(new_pos)
    print(grid)
    print(f"res: {res}")
    return ans
    
gamma = solve(lines, True)
epsilon = solve(lines, False)
print(int(gamma, 2), int(epsilon, 2))