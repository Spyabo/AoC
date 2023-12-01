txt = open("/home/spy/AoC2022/Day4/input.txt", "r")
pairs = [i for i in txt.read().strip().split("\n")]

def fully_contained(a, b):
    # Return True if a fully contains b, False otherwise
    start_a, end_a = map(int, a.split('-'))
    start_b, end_b = map(int, b.split('-'))
    
    return start_a <= start_b and end_a >= end_b

def num_fully_contained_pairs(pairs):
    # Iterate over each pair and check if one fully contains the other
    count = 0
    
    for pair in pairs:
        a, b = pair.split(',')
        if fully_contained(a, b) or fully_contained(b, a):
            count += 1
    return count

print(num_fully_contained_pairs(pairs))