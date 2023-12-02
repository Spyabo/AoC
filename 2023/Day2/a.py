with open("./2023/Day2/input.txt", "r") as f:
    lines = f.read().splitlines()

lookup = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0
games = 0
  
for i, line in enumerate(lines):
    game_id = i + 1
    turns = line.split(":")[1].split(";")
    total += game_id
   
    for turn in turns:
        flag = True
        move = turn.split(" ")[1:]
        for i in range(0, len(move), 2):
            if flag == False:
                break
            amount = int(move[i])
            colour = move[i+1].replace(",", "")
            if amount > lookup[colour]:
                total -= game_id
                flag = False
        if flag == False:
            break

    
print(total)
            