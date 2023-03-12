txt = open("/home/spy/AoC2022/Day7/testinput.txt", "r")
commands = txt.read().strip().split("\n")

root = {}
cwd = {}
stack = []

for i in range(len(commands)):
    line = commands[i]
    print(line)
    if "$ cd" in line:
        cd = line.split(" ")[-1]
        cwd[cd] = {}

    if "$ ls" in line:
        continue
    while "$" not in line:
        name = line.split(" ")[1]
        size = line.split(" ")[0]
        break

print(root)