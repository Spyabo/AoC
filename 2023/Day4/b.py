with open("./2023/Day4/input.txt", "r") as f:
    lines = f.read().splitlines()

import re

total = 0

for i, line in enumerate(lines):
    left, right = line.split(":")[1].split("|")
    winners, mine = re.findall(r"\d+", left), re.findall(r"\d+", right)
    match = set(winners) & set(mine)

    if len(match) > 0:
        total += 2 ** len(match) // 2

print(total)
