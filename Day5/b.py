import re

txt = open("/home/spy/AoC2022/Day5/input.txt", "r")

stacks = []

# Parses the crates into stacks and pops the last array full of numbers
for line in txt:
    if line == "\n": break
    stacks.append([line[k * 4 + 1] for k in range(len(line)// 4)])
stacks.pop()

# Removes the empty spaces from the stacks and reverses them for faster operations
stacks = [list("".join(c).strip()[::-1]) for c in zip(*stacks)]

# Parses the move data using regex in a,b,c to perform the required operations
for line in txt:
    a, b, c = map(int, re.findall("\\d+", line))
    stacks[c - 1].extend(stacks[b - 1][-a:])
    stacks[b - 1] = stacks[b - 1][:-a]

#prints the top element of each stack
print("".join([a[-1] for a in stacks]))