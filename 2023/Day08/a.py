with open("./2023/Day8/input.txt", "r") as f:
    lines: str = f.read().splitlines()

sequence = lines[0]
cur = "AAA"

m = {}
ans = 0

for line in lines[2:]:
    start, end = line.split(" = ")
    m[start] = tuple([end[1:4], end[6:9]])

i = 0
while True:
    l, r = m[cur]

    if i == len(sequence):
        i = 0

    if sequence[i] == "L":
        cur = l
    else:
        cur = r

    if cur == "ZZZ":
        ans += 1
        break

    ans += 1
    i += 1

print(ans)
