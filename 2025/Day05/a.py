with open('./2025/Day05/input.txt', 'r') as f:
    lines: str = f.read().splitlines()
    fresh_ranges = lines[:lines.index('')]
    ingredients = lines[lines.index('')+1:]

print(lines, fresh_ranges, ingredients)

ans = 0
used_ids = set()

for item in ingredients:
    for id_range in fresh_ranges:
        item = int(item)
        start, stop = int(id_range.split('-')[0]), int(id_range.split('-')[1])

        if start <= item <= stop:
            print(item, id_range)
            if item not in used_ids:
                ans += 1
            used_ids.add(item)
            

print(ans)