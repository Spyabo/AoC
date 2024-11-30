with open("./2023/Day5/testinput.txt", "r") as f:
    lines = list(filter(lambda x: x != "", f.read().split("\n\n")))

import re

seeds = re.findall(r"\d+", lines[0])
maps = lines[1:]
ans = []

for seed in seeds:
    seed = int(seed)
    for m in maps:
        values = re.findall(r"\d+", m)
        for i in range(0, len(values), 3):
            drs, srs, rl = int(values[i]), int(values[i + 1]), int(values[i + 2])
            if srs <= seed < srs + rl:
                seed = drs + (seed - srs)
                break

    ans.append(seed)

print(min(ans))
