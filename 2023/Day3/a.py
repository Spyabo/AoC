import re


def is_adjacent_to_symbol(line_index, number_start, number_end, lines):
    # Define the range to check in the adjacent lines
    line_range = range(max(0, line_index - 1), min(len(lines), line_index + 2))
    number_range = range(
        max(0, number_start - 1), min(len(lines[line_index]), number_end + 2)
    )

    for i in line_range:
        for j in number_range:
            # Check if the character is a special character
            if lines[i][j] not in "0123456789.":
                return True
    return False


def calculate_total(lines):
    total = 0

    for i, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            num, start, end = match.group(), match.start(), match.end()
            print(num, start, end)
            if is_adjacent_to_symbol(i, start, end - 1, lines):
                total += int(num)

    return total


# Read the file and calculate the total
with open("./2023/Day3/testinput.txt", "r") as f:
    lines = f.read().splitlines()

total = calculate_total(lines)
print(f"Total: {total}")
