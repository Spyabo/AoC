with open('./2025/Day05/input.txt', 'r') as f:
    lines: str = f.read().splitlines()
    fresh_ranges = lines[:lines.index('')]

print(fresh_ranges)

ans = 0
joined = [fresh_ranges[0]]

for id_range in fresh_ranges[1:]:
    start, stop = int(id_range.split('-')[0]), int(id_range.split('-')[1])

    new_start, new_stop = start, stop
    i = 0
    while i < len(joined):
        sta, sto = int(joined[i].split('-')[0]), int(joined[i].split('-')[1])

        if new_stop < sta or sto < new_start:
            i += 1
            continue

        new_start = min(new_start, sta)
        new_stop = max(new_stop, sto)
        joined.pop(i)

    joined.append(f"{new_start}-{new_stop}")
                

for rg in joined:
    start, stop = rg.split('-')
    ans += int(stop) - int(start) + 1

print(ans)