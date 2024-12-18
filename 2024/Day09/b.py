with open('./2024/Day09/testinput.txt', 'r') as f:
    disk: str = f.read().replace("\n", "")

mapping = []
frees = []
i = 0

for file, free in zip(disk[::2], disk[1::2]):
    mapping.extend([i] * int(file))  # File IDs
    mapping.extend([-1] * int(free))  # Blanks
    i += 1
    
if len(disk) % 2 != 0:
    mapping.extend([i] * int(disk[-1]))
    
i = 0
while i < len(mapping):
    if mapping[i] != -1:
        i += 1
        continue
    
    j = i
    while mapping[j] == -1:
        j += 1
    frees.append([i, j])
    i = j

        
print(mapping)
print(frees)

checksum = sum(i * val for i, val in enumerate(mapping) if val != -1)
print(checksum)
