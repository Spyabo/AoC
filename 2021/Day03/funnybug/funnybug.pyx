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
        
    return ans
    
def main():
    lines = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".splitlines()
    gamma = solve(lines, True)
    epsilon = solve(lines, False)
    print(int(gamma, 2), int(epsilon, 2))
    
    return (int(gamma, 2), int(epsilon, 2))

if __name__ == "__main__":
    main()