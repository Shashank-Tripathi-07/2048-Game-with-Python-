import sys
import random

""" Hello !! This is a simple 2048 mathematical game. Here's the source code, you just need to
    run it and play it""" 

""" This returns a new data structure that represents a board. It's a dictionary with keys of (x, y) tuples and values of the tile at that space. The tile is either a power-of-two integer or BLANK."""







BLANK = ''  #initializing a blank tile 

def main():
    print("Tiles with like numbers will combine into larger-numbered tiles. A new 2 tile is added to the board on each move. You win if you can create a 2048 tile. You lose if the board fills up the tiles before then.")
    input('Press Enter to start')

    GameBoard = getNewBoard()   #Creating a function called getNewBoard which has function to create a blank tile
                                # I've used bottom to top function use for this or in a tech way, reverse shot of code. 

    while True:
        drawBoard(GameBoard)                           #initializing the game 
        print('Score:', getScore(GameBoard))
        PlayerMove = askForPlayerMove()                     
        GameBoard = MakeMove(GameBoard, PlayerMove)
        addTwoToBoard(GameBoard)

        if isFull(GameBoard):
            drawBoard(GameBoard)
            print('Game Over!')
            sys.exit()

def getNewBoard():
     
    newBoard = {}                                    #building a blank dictionary, the game is built using data structures 
    for x in range(4):                               #you can change this range to change the matrix size :) 
        for y in range(4):
            newBoard[(x, y)] = BLANK                  #initializing the blank tile

    startingTwosPlaced = 0                                 # I'm generating random two 2s in the matrix in order to start the game
    while startingTwosPlaced < 2:                          
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if newBoard[randomSpace] == BLANK:                 #LOGIC: initialize the blank tiles and generate random 2s in the matrix but only till 2 twos 
            newBoard[randomSpace] = 2                      #You can tweak this to make this fill all the tiles and the code will stall :\ 
            startingTwosPlaced += 1

    return newBoard

def drawBoard(board):
    """Displays the board in a readable format."""           
    print('-' * 21)
    for y in range(4):                              
        row = []
        for x in range(4):
            tile = board[(x, y)]
            labelForThisTile = str(tile).center(5)
            row.append(labelForThisTile)
        print('|'.join(row))
    print('-' * 21)

def getScore(board):
    """Calculates and returns the current score."""
    score = 0
    for x in range(4):
        for y in range(4):
            tile = board[(x, y)]
            if tile != BLANK:
                score += board[(x, y)]       #Add the value of the tile to the score
                if tile == 2048:             #If the tile is 2048, the player wins
                    print('You win!')
                    sys.exit()
    return score

def combineTilesInColumn(column):
    """This function combines tiles and returns updated column."""  
    combinedTiles = [tile for tile in column if tile != BLANK]

    while len(combinedTiles) < 4:
        combinedTiles.append(BLANK)

    for i in range(3):
        if combinedTiles[i] == combinedTiles[i + 1] and combinedTiles[i] != BLANK:
            combinedTiles[i] *= 2
            combinedTiles[i + 1:] = combinedTiles[i + 2:] + [BLANK]

    return combinedTiles

def MakeMove(board, move):
    """Processes the player's move and returns the updated board."""
    if move == 'W':
        allColumnsSpaces = [[(x, y) for y in range(4)] for x in range(4)]
    elif move == 'A':
        allColumnsSpaces = [[(x, y) for x in range(4)] for y in range(4)]
    elif move == 'S':
        allColumnsSpaces = [[(x, y) for y in range(4)] for x in range(4)]
    elif move == 'D':
        allColumnsSpaces = [[(x, y) for x in range(4)] for y in range(4)]

    boardAfterMove = {}
    for columnSpaces in allColumnsSpaces:
        column = [board[space] for space in columnSpaces]
        combinedColumn = combineTilesInColumn(column)

        for i, space in enumerate(columnSpaces):
            boardAfterMove[space] = combinedColumn[i]

    return boardAfterMove

def askForPlayerMove():                                        
    """Prompts the player for a move and returns it."""
    print('Enter your move (WASD to move or Q to Quit):')

    while True:
        move = input('> ').upper()

        if move == 'Q':
            print("Thanks for playing!")
            sys.exit()

        if move in ('W', 'A', 'S', 'D'):
            return move

        print('Invalid move. Please enter W, A, S, D, or Q.')

def addTwoToBoard(board):
    """Adds a new '2' tile to a random empty space on the board."""
    while True:
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if board[randomSpace] == BLANK:
            board[randomSpace] = 2
            return

def isFull(board):
    """Checks if the board is full."""
    for x in range(4):
        for y in range(4):
            if board[(x, y)] == BLANK:
                return False
    return True

 #If this function is true then the tiles are full and game is over 

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()