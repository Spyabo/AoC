with open('./2025/Day03/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

ans = 0

for line_no, line in enumerate(lines):
    k = 12
    remove = len(line) - k
    stack = []
    for num in line:
        while remove and stack and stack[-1] < num:
            stack.pop()
            remove -= 1
        stack.append(num)

    if remove:
        stack = stack[:-remove]

    ans += int(''.join(stack[:k]))

print(ans)