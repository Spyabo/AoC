with open('./2024/Day02/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

safe = 0

for line in lines:
    levels = list(map(int, line.split()))

    cur = levels[0]
    if levels[1] > cur:
        increasing = True
    else:
        increasing = False
    
    for level in levels[1:]:
        if abs(level - cur) > 3 or level == cur:
            break
        
        if increasing and level < cur or not increasing and level > cur:
            break

        cur = level
    else:
        safe += 1
        
print(safe)