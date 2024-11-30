with open("./2023/Day6/input.txt", "r") as f:
    lines = f.read().splitlines()

import re

amount = []
ans = 1

times = re.findall(r"\d", lines[0])
distances = re.findall(r"\d", lines[1])
time = "".join(times)
distance = "".join(distances)

speed = 0
total = 0
for i in range(int(time)):
    time_left = int(time) - i
    travel = speed * time_left
    if travel > int(distance):
        total += 1

    speed += 1
amount.append(total)

for num in amount:
    ans *= num
print(ans)
