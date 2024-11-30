with open("./2023/Day5/input.txt", "r") as f:
    lines = list(filter(lambda x: x != "", f.read().split("\n\n")))

import re

inputs = list(map(int, re.findall(r"\d+", lines[0])))
seeds = []
maps = lines[1:]

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for m in maps:
    values = re.findall(r"\d+", m)
    new = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        for i in range(0, len(values), 3):
            drs, srs, rl = int(values[i]), int(values[i + 1]), int(values[i + 2])
            overlap_start = max(start, srs)
            overlap_end = min(end, srs + rl)
            if overlap_start < overlap_end:
                new.append((overlap_start - srs + drs, overlap_end - srs + drs))
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                if overlap_end < end:
                    seeds.append((overlap_end, end))
                break
        else:
            new.append((start, end))
    seeds = new

print(min(seeds)[0])
