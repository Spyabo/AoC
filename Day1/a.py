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

''' # 2nd attempt a few days later
cals = txt.read().strip().split("\n\n")
def max_cals(cals):    
    cur_max = 0

    for elves in cals:
        elf = list(map(int, elves.split("\n")))
        if sum(elf) > cur_max:
            cur_max = sum(elf)
    return cur_max
'''