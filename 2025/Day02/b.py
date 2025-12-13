with open('./2025/Day02/input.txt', 'r') as f:
    lines: str = f.read().replace('\n', '').split(',')

ans = 0

for id_range in lines:
    low, high = map(int, id_range.split('-'))

    if low < 10:
        continue

    for i in range(low, high+1):
        string_i = str(i)
        l, r = 0, 1

        # Find any repeating pattern (not just from the start)
        found = False
        # Only need to check pattern lengths up to half the string length
        for pattern_length in range(1, len(string_i) // 2 + 1):
            if len(string_i) % pattern_length != 0:
                continue
                
            # Try all possible starting positions for the pattern
            for start in range(len(string_i) - pattern_length + 1):
                pattern = string_i[start:start+pattern_length]
                # Check if the entire string can be built by repeating this pattern
                if len(pattern) > 0 and string_i == pattern * (len(string_i) // len(pattern)):
                    if len(pattern) < len(string_i):  # Ensure it's a proper repeat
                        print(f"{i}: {string_i} (pattern: {pattern})")
                        ans += i
                        found = True
                        break
            if found:
                break

print(ans)