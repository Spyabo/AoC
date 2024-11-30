games = open("/home/spy/AoC2022/Day2/input.txt", "r")
moves = games.readlines()

#A = {"A": "Y", "A": "X", "A": "Z"}  #win, draw, loss
#B = {"B": "Z", "B": "Y", "B": "X"}
#C = {"C": "X", "C": "Z", "C": "Y"}

def total_score(moves):
    score = 0

    for move in moves:
        first_move = move[0]
        second_move = move[2]
        #print(move[0], move[2])
        if first_move == "A":
            match second_move:
                case "Y": score += 8
                case "X": score += 4
                case "Z": score += 3
                
        elif first_move == "B":
            match second_move:
                case "Z": score += 9
                case "Y": score += 5
                case "X": score += 1
        
        elif first_move == "C":
            match second_move:
                case "X": score += 7
                case "Z": score += 6
                case "Y": score += 2
    return score

print(total_score(moves))