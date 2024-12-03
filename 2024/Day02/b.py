with open('./2024/Day02/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

safe = 0

def is_safe(levels):
    diffs = [x - y for x, y in zip(levels, levels[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)

for line in lines:
    levels = list(map(int, line.split()))
    if any(is_safe(levels[:index] + levels[index + 1:]) for index in range(len(levels))):
        safe += 1
        
print(safe)