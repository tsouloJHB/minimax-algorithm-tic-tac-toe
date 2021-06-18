import random
player1 = "x"
player2 = "o"
grid = []
player = ""
def check_positions(x,y):
   global grid
   #check xaxis
   symbol = "x"
   cal =0
   x = x+1
   y = y+1
   for d in range(0,2):

        
        if grid[2][2] == symbol and grid[2][1] == symbol and\
            grid[2][0] == symbol:
            return False
        
           
        if grid[1][1] == symbol and grid[1][0] == symbol and\
            grid[1][2] == symbol:
            return False
        
        if grid[0][0] == symbol and grid[0][1] == symbol and\
            grid[0][2] == symbol:
            return False
        
        #check yaxis
        
        if grid[2][2] == symbol and grid[1][2] == symbol and\
            grid[0][2] == symbol:
            return False
        
        if grid[1][1] == symbol and grid[0][1] == symbol and\
            grid[2][1] == symbol:
            return False
        
        if grid[0][0] == symbol and grid[1][0] == symbol and\
            grid[2][0] == symbol:
            return False
        #chech diagonal
       
    
        if grid[0][2] == symbol and grid[1][1] == symbol and\
            grid[2][0] == symbol:
            return False
        if grid[0][0] == symbol and grid[1][1] == symbol and\
            grid[2][2] == symbol:
            return False    
        symbol = "o"
   return True


def checkdraw(board):
    global grid
    #board = grid
    if check_positions(2,3):
        for x in range(0,3):
            for y in range(0,3):
                if board[x][y] == "":
                    return False
        return True
    return False                


def bestmoves():
    global grid
    global player2
    grid = create_grid()
    board = grid.copy()
    board = [["x","o","o"],["o","x","x"],["x","o","o"]]
    bestVal = -1000
    bestMove = (-1,-1)
    for t in board:
        print(t)
    
    #iterate the grid
    for a,x in enumerate(board):
        for b,y in enumerate(x):
            #check if cell is empty
            if board[a][b] == "":
                board[a][b] = player1
                #moveVal = minimax(board,0,False)
                moveVal = 0  
                board[a][b] = ""
                if moveVal > bestVal:
                    bestMove = (a,b)
                    moveVal = bestVal
    print("The best move is " ,bestMove)

    return bestMove                
    
def who_won(board):
    global grid
    #check xaxis
    symbol = "x"
    for d in range(0,2):

        
        if grid[2][2] == symbol and grid[2][1] == symbol and\
            grid[2][0] == symbol:
            return symbol
        
           
        if grid[1][1] == symbol and grid[1][0] == symbol and\
            grid[1][2] == symbol:
            return symbol
        
        if grid[0][0] == symbol and grid[0][1] == symbol and\
            grid[0][2] == symbol:
            return symbol
        
        #check yaxis
        
        if grid[2][2] == symbol and grid[1][2] == symbol and\
            grid[0][2] == symbol:
            return symbol
        
        if grid[1][1] == symbol and grid[0][1] == symbol and\
            grid[2][1] == symbol:
            return symbol
        
        if grid[0][0] == symbol and grid[1][0] == symbol and\
            grid[2][0] == symbol:
            return symbol
        #chech diagonal
       
    
        if grid[0][2] == symbol and grid[1][1] == symbol and\
            grid[2][0] == symbol:
            return symbol
        if grid[0][0] == symbol and grid[1][1] == symbol and\
            grid[2][2] == symbol:
            return symbol    
        symbol = "o"
    return ""


def minimax(board,depth,maximize_player):
    global player1
    global player2 
    #Check for winner
    #computer wins
    if check_positions(2,2) == False and player1 == who_won(board):
        return 100
    #player wins    
    if check_positions(2,2) == False and player2 == who_won(board):
        return -100

    #check for draw and return 0  
    if checkdraw(board):
        return 0
    #if maxizer wins
    
    if(maximize_player):
        bestscore = -1000
        #look for empty cells
        for i in range(0,3):
            for x in range(0,3):
                if board[i][x] == "":
                    board[i][x] = player1
                    moveVal = minimax(board,0,False)  
                    board[i][x] = ""
                    if moveVal > bestscore:
                        bestscore = moveVal
        return bestscore
    else:
        bestscore = 800
        #look for empty cells
        for i in range(0,3):
            for x in range(0,3):
                if board[i][x] == "":
                    board[i][x] = player2
                    moveVal = minimax(board,0,True)  
                    board[i][x] = ""
                    if moveVal < bestscore:
                        bestscore = moveVal
        return bestscore
    return 1

def set_postion():
    pass

def assign_players():
    global player1
    global player2
    while True:
        player1 = input("Player1 select X or O ")
        if player1.lower() == "x":
           player2 = "o"
           break
        elif player1.lower() == "o": 
           player2 = "x"
           break
        else:
           print("Player1 select X or O")

               
def check_player(player):
    global player1
    global player2
    symbol = ""
    if player == "player1":
        symbol = player1

    else:
       symbol = player2
    return symbol 


def play_game():
    play = True
    turn = ""
    move = ""
    start_player = random.randint(0,1)
    if start_player == 0:
        turn = "player1"
    else:
        turn = "player2"
             
    while play:
        if turn == "player1":
            move = input("Player1 please enter your move x,y: ")
        else:
            move = input("Player2 please enter your move x,y: ")
        #check move format 
          #if move foemat if false continue up
        try:  
            moves = move.split(",")
            a = int(moves[0])-1
            b = int(moves[1])-1 
            if a  < -1 or a > 1 or b  < -1 or b > 1:
                print("Incorrect corodinates given")
                continue
        except ValueError:
            print("Incorrect format")
            continue  
        update_grid(move,turn)
        draw_grid()
        print(who_won([],"player1")) 
        #minimax([],2,False)  
        if check_positions(a,b) == False:
           break         
        if turn == "player1":
           turn = "player2"
        else:
           turn = "player1"
   
        
        """   
        if(checkdraw()):
            print("its a draw") 
        """      
    print(turn," won",)
    print("") 
 
def create_grid():
    grid = [["" for x in range(0,3)] for i in range(0,3)]
    return grid    

	
def update_grid(move,player):
    global grid
    moves = move.split(",")
    a = int(moves[0])
    b = int(moves[1]) 
    symbol = check_player(player)
    grid[a][b] = symbol
    

def draw_grid():
    global grid
    print("")
    for a in range(0,3):
       print("    ",a,end="") 
    print("")
    print("")
    var  = " " 
    for x,z in enumerate(grid):
        print("",x,end="")
        print(" ",z[0] if z[0]!=""else " "," |",end="")
        print("  ",z[1] if z[1]!=""else " ","  |",end="")   
        print("  ",z[2] if z[2]!=""else " ","",end="")
        print("")
        if x < 2:
            for i,l in enumerate(z):
               
               if i == 1:  
                   print("|",end="") 
               if i != 0:            
                   print("_______",end="")
               else:     
                    print("   ____",end="") 
               if i == 1:
                   print("|",end="")     
        print("")
        if x < 2:   
            print("       |",end="")
            print("       |",end="")        
        print("")

def reset():
    global grid 
    global player1
    global player2
    grid = []
    player1 = ""
    player2 = ""



def menu():
    stop = False
    while stop == False:
        print("** MENU **")
        print("")
        print("1. Start game")
        print("2. exit")
        print("")
        click = int(input("Enter command: "))
        if click == 1:
            reset()
            start_game()
        elif click == 2:
            break
        else:
            continue    
def gameloop():
    print("")
    print("************************************* Tic tac toe ********************************************")
    menu()

def start_game():
    global grid
    assign_players()
    grid = create_grid()
    draw_grid() 
    play_game()

#board = [["x","","o"],["o","","x"],["x","","x"]]
#grid = board
#minimax(board,4,True)
#gameloop()
bestmoves()
