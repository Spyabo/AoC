txt = open("/home/spy/AoC2022/Day3/testinput.txt", "r")
rucksacks = txt.read().strip()

def score_calc(dups: str):
    total = 0
    for char in dups:
        if char.isupper() == True:
            total += ord(char) - 38
        if char.islower() == True:
            total += ord(char) - 96
    return total

def duplicates(rucksacks):
    rucksack = rucksacks.split("\n")
    
    start = 0
    stop = 3

    for sets in rucksack:
        group = rucksack[start:stop]
        start +=  3
        stop += 3
        print(group)
            

print(duplicates(rucksacks))