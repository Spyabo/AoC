with open("./2023/Day4/input.txt", "r") as f:
    lines = f.read().splitlines()

import re
from collections import defaultdict

copies = defaultdict(list)

for i, line in enumerate(lines):
    if i not in copies:
        copies[i] = 1

    left, right = line.split(":")[1].split("|")
    winners, mine = re.findall(r"\d+", left), re.findall(r"\d+", right)
    match = set(winners) & set(mine)

    if len(match) > 0:
        for j in range(i + 1, i + len(match) + 1):
            copies[j] = copies.get(j, 1) + copies[i]

print(sum(copies.values()))
