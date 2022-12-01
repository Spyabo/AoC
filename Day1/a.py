cals = open("/home/spy/AoC2022/Day1/input.txt", "r")

def max_cals(cals) -> int:
    elf = []
    current_max = 0
    for line in cals:
        if line == "\n":
            if sum(elf) > current_max:
                current_max = sum(elf)
            elf.clear()
        elif line.strip() != '':
            elf.append(int(line.strip()))
    return current_max

print(max_cals(cals))