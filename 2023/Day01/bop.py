with open("./2023/Day1/input.txt", "r") as f:
    lines = f.read().splitlines()

total = 0

lookup = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for line in lines:
    l = 0
    r = len(line) - 1
    l_num = ""
    r_num = ""
    l_buffer = ""
    r_buffer = ""

    while True:
        if line[l].isdigit():
            l_num = line[l]
        else:
            l_buffer += line[l]

        if line[r].isdigit():
            r_num = line[r]
        else:
            r_buffer += line[r]

        for key, val in lookup.items():
            if key in l_buffer:
                l_num = val

            if key in r_buffer[::-1]:
                r_num = val

        print(
            f"line: {line} l_num: {l_num} r_num: {r_num} l_buffer: {l_buffer} r_buffer: {r_buffer[::-1]}"
        )

        if l_num != "" and r_num != "":
            total += int(l_num + r_num)
            print(int(l_num + r_num))
            break

        if l_num == "":
            l += 1
        if r_num == "":
            r -= 1

print(total)
