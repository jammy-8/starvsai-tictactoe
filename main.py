grid = []
line = []
for i in range (3):
    for j in range (3):
        line.append(" ")
    grid.append(line)
    line = []

def print_grid():
    for i in range(3):
        print("|", end ="")
        for j in range(3):
            print (grid[i][j], "|", end ="")
        print("")
        
def player_turn(turn_player1):
    if turn_player1 == True:
        turn_player1 = False
        print(f"It's {player2}'s turn")
    else:
        turn_player1 = True
        print(f"It's {player1}'s turn")        
    return turn_player1

