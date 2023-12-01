cals = open("/home/spy/AoC2022/Day1/input.txt", "r")

def max_cals(cals) -> int:
    elf = []
    maxs = [0,0,0]
    for line in cals:
        if line == "\n":
            if sum(elf) > maxs[-1]:
                maxs[-1] = sum(elf)
            elf.clear()
            maxs.sort(reverse=True)
        elif line.strip() != '':
            elf.append(int(line.strip()))
    return sum(maxs)

print(max_cals(cals))