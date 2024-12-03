with open('./2024/Day03/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

import re

res = 0
last_command = "do"

for line in lines:
    # Find strings in the format "mul(x, y) | don't() | do()"
    matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)", line)

    for match in matches:
        instruction = match.group()

        if instruction == "do()":
            last_command = "do"
        elif instruction == "don't()":
            last_command = "don't"
        elif instruction.startswith("mul") and last_command == "do":
            x, y = match.groups()
            res += int(x) * int(y)

print(res)
