import sys
import random

BLANK = ''

def main():
    print("Tiles with like numbers will combine into larger-numbered tiles. A new 2 tile is added to the board on each move. You win if you can create a 2048 tile. You lose if the board fills up the tiles before then.")
    input('Press Enter to start')

    GameBoard = getNewBoard()
    score = 0                          # Initialize score to 0

  
    while True:
        drawBoard(GameBoard)
        print('Score:', score)  # Display the current score
        PlayerMove = askForPlayerMove()
        GameBoard = MakeMove(GameBoard, PlayerMove)
        score = getScore(GameBoard)  # Update the score after the move
        addTwoToBoard(GameBoard)

        if isFull(GameBoard):
            drawBoard(GameBoard)
            print('Game Over!')
            print('Final Score:', score)  # Display the final score
            sys.exit()

def getNewBoard():
    """Returns a new data structure representing a board."""
    newBoard = {}
    for x in range(4):
        for y in range(4):
            newBoard[(x, y)] = BLANK

    startingTwosPlaced = 0
    while startingTwosPlaced < 2:
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if newBoard[randomSpace] == BLANK:
            newBoard[randomSpace] = 2
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
                score += board[(x, y)]
                if tile == 2048:
                    print('You win!')
                    sys.exit()
    return score

def combineTilesInColumn(column):
    """Combines tiles in a single column."""
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
    if move == 'W':  # Move up
        allColumnsSpaces = [[(x, y) for y in range(4)] for x in range(4)]
    elif move == 'A':  # Move left
        allColumnsSpaces = [[(x, y) for x in range(4)] for y in range(4)]
    elif move == 'S':  # Move down
        allColumnsSpaces = [[(x, y) for y in range(3, -1, -1)] for x in range(4)]
    elif move == 'D':  # Move right
        allColumnsSpaces = [[(x, y) for x in range(3, -1, -1)] for y in range(4)]

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

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
