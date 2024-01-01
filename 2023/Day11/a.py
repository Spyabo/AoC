with open("./2023/Day11/testinput.txt", "r") as f:
    lines: str = f.read().splitlines()


expand_row = []
expand_col = []
galaxies = []
num_galaxies = 0

for i, row in enumerate(lines):
    if "#" not in row:
        expand_row.append(i)
    else:
        num_galaxies += row.count("#")

for i in range(len(lines[0])):
    col = []
    for j in range(len(lines)):
        col.append(lines[j][i])
    if "#" not in col:
        expand_col.append(i)

for i, pos in enumerate(expand_row):
    lines.insert(pos + i, "." * len(lines[0]))

print(expand_row, expand_col)

for i, pos in enumerate(expand_col):
    for j, row in enumerate(lines):
        lines[j] = row[: pos + i] + "." + row[pos + i :]

for i, row in enumerate(lines):
    for j, char in enumerate(row):
        if char == "#":
            galaxies.append((j, i))


# print(galaxies)8
print(lines)
distance = 0
for i in range(len(galaxies) - 1):
    matching = galaxies[i]
    pairs = galaxies[i + 1 :]
    # print(pairs)
    for pair in pairs:
        # print(matching, pair)
        distance += abs(matching[0] - pair[0]) + abs(matching[1] - pair[1])
print(distance)
