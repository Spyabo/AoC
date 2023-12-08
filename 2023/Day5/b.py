with open("./2023/Day5/input.txt", "r") as f:
    lines = list(filter(lambda x: x != "", f.read().split("\n\n")))

import re

seeds = list(map(int, re.findall(r"\d+", lines[0])))
seeds = list(range(seeds[0], seeds[0] + seeds[1]))
maps = lines[1:]
ans = []

for seed in seeds:
    for m in maps:
        values = re.findall(r"\d+", m)
        for i in range(0, len(values), 3):
            drs, srs, rl = int(values[i]), int(values[i + 1]), int(values[i + 2])
            if srs <= seed < srs + rl:
                seed = drs + (seed - srs)
                break

    ans.append(seed)

print(min(ans))
