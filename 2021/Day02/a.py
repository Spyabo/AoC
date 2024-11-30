with open('./2021/Day02/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

x = 0
y = 0

for line in lines:
    direction, distance = line.split(' ')
    if direction == 'forward':
        x += int(distance)
    elif direction == 'down':
        y += int(distance)
    elif direction == 'up':
        y -= int(distance)

print(x * y)