games = open("./input.txt", "r")
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
                case "Y": score += 4
                case "X": score += 3
                case "Z": score += 8
                
        elif first_move == "B":
            match second_move:
                case "Z": score += 9
                case "Y": score += 5
                case "X": score += 1
        
        elif first_move == "C":
            match second_move:
                case "X": score += 2
                case "Z": score += 7
                case "Y": score += 6
    return score

print(total_score(moves))