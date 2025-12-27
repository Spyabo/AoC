with open('./2025/Day02/testinput.txt', 'r') as f:
    lines: str = f.read().replace('\n', '').split(',')

ans = 0

for id_range in lines:
    low, high = map(int, id_range.split('-'))

    if low < 10:
        continue

    for i in range(low, high+1):
        string_i = str(i)
        l, r = 0, 1
        pattern = False

        while r < len(string_i) // 2:
            if string_i[l] == string_i[r]:
                pattern = True
            
            r += 1

        if pattern:
            repeater = string_i[l:r]
            slices = string_i.split(repeater)
            print(repeater, string_i, slices)

print(ans)