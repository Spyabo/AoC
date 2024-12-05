with open('./2024/Day05/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

from collections import defaultdict

rules = defaultdict(list)
i = 0

while lines[i] != '':
    left, right = lines[i].split('|')
    rules[left].append(right)
    
    i += 1
    
updates = lines[i + 1:]    
total = 0

for update in updates:
    update = update.split(",")
    valid = True
    
    for index, page in enumerate(update):
        for rule in rules[page]:
            if rule in update and index > update.index(rule):
                print(f"Update: {update} Page: {page} Rule: {rule}, {int(update[len(update) // 2])}")
                valid = False
                break
        else:
            continue
        break
    
    if valid: total += int(update[len(update) // 2])

print(total)