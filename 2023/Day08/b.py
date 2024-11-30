from functools import reduce
from math import gcd

with open("./2023/Day8/input.txt", "r") as f:
    lines: str = f.read().splitlines()

sequence = lines[0]

m = {}
starts = []
time = []
ans = 0

for line in lines[2:]:
    start, end = line.split(" = ")
    m[start] = tuple([end[1:4], end[6:9]])

    if start[-1] == "A":
        starts.append(start)

for index, start in enumerate(starts):
    i = 0
    ans = 0
    cur = start
    while cur[-1] != "Z":
        if i == len(sequence):
            i = 0

        l, r = m[cur]

        if sequence[i] == "L":
            cur = l
        else:
            cur = r

        i += 1
        ans += 1

    starts[index] = ans
    print(starts)

lcm = starts.pop()

for num in starts:
    lcm = (lcm * num) // gcd(lcm, num)

print(lcm)
