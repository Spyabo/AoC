with open('./2024/Day09/input.txt', 'r') as f:
    disk: str = f.read().replace("\n", "")

mapping = []
i = 0

for file, free in zip(disk[::2], disk[1::2]):
    mapping.extend([i] * int(file))  # File IDs
    mapping.extend([-1] * int(free))  # Blanks
    i += 1
    
if len(disk) % 2 != 0:
    mapping.extend([i] * int(disk[-1]))

l, r = 0, len(mapping) - 1
while l <= r:
    if mapping[l] != -1:
        l += 1
        continue
    while mapping[r] == -1:
        r -= 1
    if r < l:
        break
    mapping[l] = mapping[r]
    mapping[r] = -1 
    l += 1

checksum = sum(i * val for i, val in enumerate(mapping) if val != -1)
print(checksum)
