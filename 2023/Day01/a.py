with open("input.txt", "r") as f:
    lines = f.read().splitlines()

total = 0

for line in lines:
    l = 0
    r = len(line) - 1
    l_num = ""
    r_num = ""

    while True:
        if line[l].isdigit():
            l_num = line[l]
        if line[r].isdigit():
            r_num = line[r]
        if l_num != "" and r_num != "":
            total += int(l_num + r_num)
            break

        if l_num == "":
            l += 1
        if r_num == "":
            r -= 1

print(total)
