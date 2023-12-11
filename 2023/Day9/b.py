with open("./2023/Day9/input.txt", "r") as f:
    lines = f.read().splitlines()

ans = 0


def diff_calc(seq):
    if all(x == 0 for x in seq):
        return 0

    diff = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
    diff = diff_calc(diff)
    return seq[0] - diff


for line in lines:
    nums = list(map(int, line.split()))
    ans += diff_calc(nums)

print(ans)
