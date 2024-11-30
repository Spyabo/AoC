with open('./2021/Day03/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

grid = [[] for x in range(len(lines[0]))]

for line in lines:
    for i, c in enumerate(line):
        grid[i].append(c)
        
gamma = ""

for pos in grid:
    gamma += max(set(pos), key=pos.count)

# Calculate the complement
epsilon = bin(~int(gamma, 2) & ((1 << len(gamma)) - 1))[2:].zfill(len(gamma))

print(int(gamma, 2) * int(epsilon, 2))
