with open('./2021/Day03/input.txt', 'r') as f:
    lines: str = f.read().splitlines()

def solve(input, bool):
    for i in range(len(input[0])):
        vert = []

        for j in range(len(input)):
            vert.append(input[j][i])

        highest = max(set(vert), key=vert.count)
        lowest = min(set(vert), key=vert.count)
        
        if highest == lowest:
            highest = "1"
            lowest = "0"
        
        keep = highest if bool else lowest
        print(f"keep {keep} at {i} \n")
        
        input = list(filter(lambda x: x[i] == keep, input))
        print(input, "\n")
            
        if len(input) == 1:
            return int(input[0], 2)
        
    return "Something went wrong!"
            
print(solve(lines, True) * solve(lines, False))