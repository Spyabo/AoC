with open('./input.txt', 'r') as f:
    lines: str = f.read().splitlines()

safe = 0

for line in lines:
    levels = list(map(int, line.split()))

    cur = levels[0]

    for level in levels[1:]:
        if level > cur:
            increasing = True
        else:
            increasing = False

        

