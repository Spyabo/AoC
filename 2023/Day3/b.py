import re


def is_adjacent_to_star(line_index, number_start, number_end, lines):
    # Define the range to check in the adjacent lines
    line_range = range(max(0, line_index - 1), min(len(lines), line_index + 2))
    number_range = range(
        max(0, number_start - 1), min(len(lines[line_index]), number_end + 2)
    )

    for i in line_range:
        for j in number_range:
            # Check if the char is a *
            if lines[i][j] == "*":
                return True, i, j
    return False, -1, -1


def calculate_total(lines):
    matches = {}
    for i, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            num, start, end = match.group(), match.start(), match.end()
            # print(num, start, end)
            result, x, y = is_adjacent_to_star(i, start, end - 1, lines)
            # print(result, x, y)
            if result:
                if (x, y) in matches:
                    matches[(x, y)].append(int(num))
                else:
                    matches[(x, y)] = [int(num)]
    # print(matches)
    # multiply all the numbers in the matches that have an array length of two
    return sum([x[0] * x[1] for x in matches.values() if len(x) == 2])


# Read the file and calculate the total
with open("./2023/Day3/input.txt", "r") as f:
    lines = f.read().splitlines()

total = calculate_total(lines)
print(f"Total: {total}")
