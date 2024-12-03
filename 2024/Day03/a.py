with open('./2024/Day03/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

import re

res = 0

for line in lines:
    # Find strings in the format "mul(x, y)"
    muls = re.findall(r"mul\((\d+),(\d+)\)", line)
    
    for mul in muls:
        res += int(mul[0]) * int(mul[1])

print(res)