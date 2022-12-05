txt = open("/home/spy/AoC2022/Day3/input.txt", "r")
rucksacks = [i for i in txt.read().strip().split("\n")]

def score_calc(badge):
    total = 0

    for char in badge:
        if char.isupper() == True:
            total += ord(char) - 38
        if char.islower() == True:
            total += ord(char) - 96
    return total

def duplicates(rucksacks):
    ans = 0

    for i in range(0, len(rucksacks), 3):
        group = rucksacks[i:(i+3)]
        badge = set(group[0]) & set(group[1]) & set(group[2])
        ans += score_calc(badge)
    return ans

print(duplicates(rucksacks))