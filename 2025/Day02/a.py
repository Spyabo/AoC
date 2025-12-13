with open('./2025/Day02/input.txt', 'r') as f:
    lines: str = f.read().replace('\n', '').split(',')

ans = 0

for id_range in lines:
    low, high = map(int, id_range.split('-'))

    for i in range(low, high+1):
        string_i = str(i)

        if len(string_i) % 2 != 0:
            continue

        if string_i[:len(string_i)//2] == string_i[len(string_i)//2:]:
            ans+=i

print(ans)