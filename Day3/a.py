txt = open("/home/spy/AoC2022/Day3/input.txt", "r")
rucksacks = txt.readlines()

def score_calc(dups: str):
    total = 0
    for char in dups:
        if char.isupper() == True:
            total += ord(char) - 38
        if char.islower() == True:
            total += ord(char) - 96
    return total

def duplicates(rucksacks):

    items = set()
    dups = set()
    ans = 0

    for rucksack in rucksacks:
        first_half = rucksack[:len(rucksack)//2]
        second_half = rucksack[len(rucksack)//2:]
        for char in first_half:
            items.add(char)
        for char in second_half:
            if char in items:
                dups.add(char)
        ans += score_calc(dups)
        items.clear()
        dups.clear()
    return ans

print(duplicates(rucksacks))
