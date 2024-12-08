with open('./2024/Day07/testinput.txt', 'r') as f:
    lines: str = f.read().splitlines()

numbers = [x for x in range(10)]
skip_numbers = [6, 2]

total = 0

for number in numbers:
    if number in skip_numbers:
        print(f"Skipping {number}")
        continue
    
    print(number)
    total = total + number
    
print(total)