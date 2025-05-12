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

def win_check(grid, player1_symbol, player2_symbol):
    full_grid = True
    player1_symbol_count = 0
    player2_symbol_count = 0
        
    for i in range(3):
        for j in range(3):
            if grid[i][j] == player1_symbol:
                player1_symbol_count += 1
                player2_symbol_count = 0
                if player1_symbol_count == 3:
                    game = False
                    winner = player1
                    return game, winner
            if grid[i][j] == player2_symbol:
                player2_symbol_count += 1
                player1_symbol_count = 0
                if player2_symbol_count == 3:
                    game = False
                    winner = player2
                    return game, winner
            if grid[i][j] == " ":
                full_grid = False
                 
        player1_symbol_count = 0
        player2_symbol_count = 0
    
    player1_symbol_count = 0
    player2_symbol_count = 0    
    for i in range (3):
        for j in range (3):
            for k in range (3):
                if i + k <= 2:
                    if grid[i + k][j] == player1_symbol:
                        player1_symbol_count += 1
                        player2_symbol_count = 0
                        if player1_symbol_count == 3:
                            game = False
                            winner = player1
                            return game, winner
                    if grid[i + k][j] == player2_symbol:
                        player2_symbol_count += 1
                        player1_symbol_count = 0
                        if player2_symbol_count == 3:
                            game = False
                            winner = player2
                            return game, winner
            if grid[i][j] == " ":
                full_grid = False
 
            player1_symbol_count = 0
            player2_symbol_count = 0
    
    player1_symbol_count = 0
    player2_symbol_count = 0    
    for i in range (3):
        for j in range (3):
            for k in range (3):
                if j + k <= 2 and i + k <= 2:
                    if grid[i + k][j + k] == player1_symbol:
                        player1_symbol_count += 1
                        player2_symbol_count = 0
                        if player1_symbol_count == 3:
                            game = False
                            winner = player1
                            return game, winner
                    if grid[i + k][j + k] == player2_symbol:
                        player2_symbol_count += 1
                        player1_symbol_count = 0
                        if player2_symbol_count == 3:
                            game = False
                            winner = player2
                            return game, winner
            if grid[i][j] == " ":
                full_grid = False
             
            player1_symbol_count = 0
            player2_symbol_count = 0
             
    player1_symbol_count = 0
    player2_symbol_count = 0    
    for i in range (3):
        for j in range (3):
            for k in range (3):
                if j - k >= 0 and i + k <= 2:
                    if grid[i + k][j - k] == player1_symbol:
                        player1_symbol_count += 1
                        player2_symbol_count = 0
                        if player1_symbol_count == 3:
                            game = False
                            winner = player1
                            return game, winner
                    if grid[i + k][j - k] == player2_symbol:
                        player2_symbol_count += 1
                        player1_symbol_count = 0
                        if player2_symbol_count == 3:
                            game = False
                            winner = player2
                            return game, winner
            if grid[i][j] == " ":
                full_grid = False
         
            player1_symbol_count = 0
            player2_symbol_count = 0   
        
    if full_grid == True:
        game = False
        winner = ""
        return game, winner
    else:
        game = True
        winner = ""
        return game, winner

while game == True:
    turn_player1 = player_turn(turn_player1)
    free_box = False
    while free_box == False:
        cell = int(input("Please enter a number for your case (1 to 9 from left to right and from top to bottom) : "))
        free_box = free_cell(cell)
    grid = write_cell(cell) 
    print("")
    print_grid()
    game, winner = win_check(grid, player1_symbol, player2_symbol)
    if game == False:
        break

if winner == player1:
    print(f"Winner is {player1} !")
elif winner == player2:
    print(f"Winner is {player2} !")
else:
    print(f"Grid is full : equality for {player1} and {player2} !")
