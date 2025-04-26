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

def write_cell(cell):
    cell -= 1
    i = int(cell / 3)
    j =  cell % 3   
    if turn_player1 == True:
        grid[i][j] = player1_symbol
    else:
        grid[i][j] = player2_symbol
    return grid

def free_cell(cell):
    cell -= 1
    i = int(cell / 3)
    j =  cell % 3
    if grid[i][j] == player1_symbol or grid[i][j] == player2_symbol:
        print("This cell is not free")
        return False
    return True

print("Welcome to the Star vs AI !")
print("")
print_grid()
print("")
player1 = input("Please enter name of Star : ")
player1_symbol = input("Please enter the symbol of Star : ")
player2 = input("Please enter name of AI : ")
player2_symbol = input("Please enter the symbol of AI : ")
game = True
full_grid = False
turn_player1 = False
winner = ""
