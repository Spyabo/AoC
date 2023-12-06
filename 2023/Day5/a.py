with open("./2023/Day5/input.txt", "r") as f:
    lines = list(filter(lambda x: x != "", f.read().splitlines()))

import re

seeds = re.findall(r"\d+", lines[0])
ans = []

for seed in seeds:
    seed = int(seed)
    for i, line in enumerate(lines[1:]):
        values = re.findall(r"\d+", line)
        if values == []:
            continue
        drs, srs, rl = int(values[0]), int(values[1]), int(values[2])
        if seed in range(srs, srs + rl):
            # sources = [x for x in range(srs, srs + rl)]
            # destinations = [x for x in range(drs, drs + rl)]
            seed = drs + (seed - srs)

    ans.append(seed)

print(min(ans))
