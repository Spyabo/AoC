with open('./2021/Day01/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

ans = 0
cur = int(lines[0])

for line in lines[1:]:
    if int(line) > cur:
        ans += 1
    cur = int(line)

print(ans)
