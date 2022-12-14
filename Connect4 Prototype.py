import random

def connect4():
    player1 = 1
    player2 = 2
    # set up empty board
    board = []
    for i in range(6):
        board.append([0] * 7)
        
    # coin filp who goes first
    if random.randint(0, 1) == 0:
        print('Player 1 goes first.')
        player = 1
    else:
        print('Player 2 goes first.')
        player = 2
        
    # main game loop
    while True:
        
        # print current board
        printBoard(board)
        
        # get player's move
        if player == 1:
            move = getPlayerMove(board, player1)
        else:
            move = getPlayerMove(board, player2)
            
        # make move
        makeMove(board, player, move)
        
        # check for winner
        if isWinner(board, player):
            printBoard(board)
            print('Winner Winner Chicken Dinner!')
            print('Player ' + str(player) + ' wins!')
            break
        
        # check for draw
        if isFull(board):
            printBoard(board)
            print('Draw!')
            break
        
        # switch players
        if player == 1:
            player = 2
        else:
            player = 1
            
            
# print the current board            
def printBoard(board):
    for x in range(6):
        for y in range(7):
            if board[x][y] == 0:
                print('_', end=' ')
            elif board[x][y] == 1:
                print('X', end=' ')
            else:
                print('O', end=' ')
        print()
    print()
    

# get a move from the player    
def getPlayerMove(board, player):
    while True:
        print('Player ' + str(player) + ', enter your move (1-7): ', end='')
        move = int(input())
        if isValidMove(board, move):
            return move
        else:
            print('Invalid move. Try again.')
            

# make the given move on the board            
def makeMove(board, player, move):
    for x in range(6):
        if board[x][move - 1] == 0:
            board[x][move - 1] = player
            return
            
            
# return True if the given move is valid, False otherwise            
def isValidMove(board, move):
    if move < 1 or move > 7:
        return False
    
    if board[5][move - 1] != 0:
        return False

    return True
    
    
# return True if the board is full, False otherwise    
def isFull(board):
    for x in range(6):
        for y in range(7):
            if board[x][y] == 0:
                return False
    return True
    
    
# return True if the given player has won, False otherwise
# It just works
def isWinner(board, player):
    # check rows
    for x in range(6):
        for y in range(4):
            if board[x][y] == player and board[x][y + 1] == player and board[x][y + 2] == player and board[x][y + 3] == player:
                return True
            
    # check columns
    for x in range(3):
        for y in range(7):
            if board[x][y] == player and board[x + 1][y] == player and board[x + 2][y] == player and board[x + 3][y] == player:
                return True
            
    # check diagonals
    for x in range(3):
        for y in range(4):
            if board[x][y] == player and board[x + 1][y + 1] == player and board[x + 2][y + 2] == player and board[x + 3][y + 3] == player:
                return True
            
    for x in range(3):
        for y in range(4):
            if board[5 - x][y] == player and board[4 - x][y + 1] == player and board[3 - x][y + 2] == player and board[2 - x][y + 3] == player:
                return True
                
    return False

# main function
connect4()

