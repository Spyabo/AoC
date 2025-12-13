with open('./2025/Day03/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

ans = 0

for line in lines:
    biggest = max(line[:-1])
    second_biggest = max(line[line.index(biggest)+1:])
    ans += int(biggest + second_biggest)

print(ans)
