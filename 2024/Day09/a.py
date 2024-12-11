with open('./2024/Day09/input.txt', 'r') as f:
    disk: str = f.read().replace("\n", "")

mapping = ""
i = 0

for file, free in zip(disk[::2], disk[1::2]):
    mapping += f"{int(file)*str(i)}{int(free)*"."}"
    i += 1
else:
    mapping += int(disk[-1])*str(i)


# print(mapping)

l, r = 0, len(mapping) - 1

while l < r:
    if mapping[l] != ".":
        l += 1
        continue
    
    # Swich the chars at l and r
    mapping = mapping[:l] + mapping[r] + mapping[l+1:r] + mapping[l] + mapping[r+1:]
    # print(mapping)
    l += 1
    while mapping[r] == ".":
        r -= 1
    
# print(mapping)

checksum = sum([int(i)*int(id_num) for i, id_num in enumerate(mapping) if id_num != "."])
print(checksum)