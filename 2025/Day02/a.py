with open('./2025/Day02/testinput.txt', 'r') as f:
    lines: str = f.read().replace('\n', '').split(',')

for id_range in lines:
    low, high = map(int, id_range.split('-'))
    