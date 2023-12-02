with open("./2023/Day2/input.txt", "r") as f:
    lines = f.read().splitlines()

games = []
total = 0

for i, line in enumerate(lines):
    turns = line.split(":")[1].split(";")
    
    max_green = 0
    max_blue = 0
    max_red = 0
   
    for turn in turns:
        move = turn.split(" ")[1:]
        for i in range(0, len(move), 2):
            amount = int(move[i])
            colour = move[i+1].replace(",", "")
            
            if colour == "red":
                max_red = max(max_red, amount)
            if colour == "blue":
                max_blue = max(max_blue, amount)
            if colour == "green":
                max_green = max(max_green, amount)
           
    games.append((max_red, max_green, max_blue))

for game in games:
    total += game[0] * game[1] * game[2]

print(total)
            