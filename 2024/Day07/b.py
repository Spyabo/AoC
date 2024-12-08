with open('./2024/Day07/input.txt', 'r') as f:
    lines = f.read().splitlines()

import itertools

def evaluate_expression(numbers, operators):
    current_value = int(numbers[0])
    for i, op in enumerate(operators):
        if op == "+":
            current_value += int(numbers[i + 1])
        elif op == "*":
            current_value *= int(numbers[i + 1])
        elif op == "||":
            current_value = int(str(current_value) + str(numbers[i + 1]))
    
    return current_value

def generate_equations(operators, num_numbers):
    return itertools.product(operators, repeat=num_numbers - 1)

ans = 0
operators = ["*", "+", "||"]

for line in lines:
    target, numbers = line.split(": ")
    target = int(target)
    numbers = numbers.split(" ")
    
    # Generate all possible operator combinations
    operator_combinations = generate_equations(operators, len(numbers))
    
    for combo in operator_combinations:
        result = evaluate_expression(numbers, combo)
        
        if result == target:
            ans += result
            break

print(ans)
