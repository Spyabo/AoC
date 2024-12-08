with open('./2024/Day07/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

import re
import itertools

ans = 0

def generate_equations(operators, numbers):
    operator_combinations = list(itertools.product(operators, repeat=len(numbers) - 1))
    all_expressions = []
    
    for combo in operator_combinations:
        expression = numbers[0]
        for i, op in enumerate(combo):
            if op == "+":
                # Wrap addition in parentheses
                expression = f"({expression}+{numbers[i + 1]})"
            else:
                # No wrapping for multiplication
                expression = f"{expression}*{numbers[i + 1]}"
        all_expressions.append(expression)
    
    return all_expressions

for line in lines:
    target, numbers = int(line.split(": ")[0]), line.split(": ")[1].split(" ")
    combos = generate_equations(["*", "+"], numbers)

    for combo in combos:
        cur_total = eval(combo)
        
        if cur_total == target:
            ans += cur_total
            break
        
print(ans)