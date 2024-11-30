with open('./2021/Day01/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

ans = 0
cur = [int(lines[0]), int(lines[1]), int(lines[2])]

for i, line in enumerate(lines[:-3]):
    compare = [int(lines[i + 1]), int(lines[i + 2]), int(lines[i + 3])]
    
    if sum(cur) < sum(compare):
        ans += 1
    
    cur = [int(lines[i + 1]), int(lines[i + 2]), int(lines[i + 3])]

print(ans)