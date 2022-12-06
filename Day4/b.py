txt = open("/home/spy/AoC2022/Day4/input.txt", "r")
pairs = [i for i in txt.read().strip().split("\n")]

def contained(a, b):
    # Return True if a fully contains b, False otherwise
    start_a, end_a = map(int, a.split('-'))
    start_b, end_b = map(int, b.split('-'))
    
    return (start_a <= start_b <= end_a) or (start_b <= start_a <= end_b)

def num_overlapping_pairs(pairs):
    # Iterate over each pair and check if one fully contains the other
    count = 0
    
    for pair in pairs:
        a, b = pair.split(',')
        if contained(a, b) or contained(b, a):
            count += 1
    return count

print(num_overlapping_pairs(pairs))