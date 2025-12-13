with open('./2025/Day03/testinput.txt', 'r') as f:
    lines: str = f.read().splitlines()

ans = 0

for line in lines:
    joltage = max(line[:-11])
    largest = max(line[:-11])
    length = 10
    while len(joltage) < 11:
        line = line[line.index(largest)+1:]
        largest = max(line[:-length])
        joltage += largest
        length -= 1

    joltage += max(line)
    ans += int(joltage)

print(ans)