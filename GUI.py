"""
2015/XX/XX

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
This part of the game is in charge of prompting the user for input & displaying it out on a graphical overlay while allowing user input
"""
import turtle
import time
import math
import os.path
import copy
from ASCII import printOutASCII
import ReversiBoard

# Initialize global constants (necessary for when functions are called from a different file)
HALF_BOARD_WIDTH = -250.0
HALF_BOARD_HEIGHT = -HALF_BOARD_WIDTH
BOARD_OUTLINE_COLOUR = "White"
BOARD_BACKGROUND_COLOUR = "Brown"
PLAYER_1_COLOUR = "White"
PLAYER_2_COLOUR = "Black"

# Initialize global mutable object from ReversiBoard
backend = ReversiBoard

# Initialize the global mutable display out & mutable turtles for the board, pieces, and ghost pieces
displayOut = turtle.Screen()
boardTurtle = turtle.Turtle()
pieceTurtle = turtle.Turtle()
ghostPieceTurtle = turtle.Turtle()


# Function to print out the ASCII intro to the display overlay & waits 10 seconds before running the program
def printOutIntro(inputTurtle):
    teleportToTile(6, 1, inputTurtle)
    inputTurtle.write(printOutASCII(), align="Left", font=("Arial", int(abs(HALF_BOARD_WIDTH) * 1 / 25)))
    time.sleep(0)
    inputTurtle.clear()


# Function to print out the reversi table. Clears display before printing and sets color to contrast BG
# Takes no params, accesses global variable BOARD_OUTLINE_COLOUR
def printOutTable(inputTurtle):
    inputTurtle.clear()
    inputTurtle.color(BOARD_OUTLINE_COLOUR)

    # For loop to teleport the turtle through generating the board. Starts top left
    for indexCounter in range(9):
        # Lift turtle and teleport to left hand side of the following row, top left if first row
        # Then draw line
        inputTurtle.up()
        inputTurtle.goto(HALF_BOARD_WIDTH, HALF_BOARD_HEIGHT - indexCounter * HALF_BOARD_HEIGHT / 4)
        inputTurtle.down()
        inputTurtle.forward(-HALF_BOARD_WIDTH * 2)

        # Turn turtle to print column line, follows same steps as above
        # Then turns the turtle back to the horizontal for the next row
        inputTurtle.right(90)
        inputTurtle.up()
        inputTurtle.goto(HALF_BOARD_WIDTH - indexCounter * HALF_BOARD_WIDTH / 4, HALF_BOARD_HEIGHT)
        inputTurtle.down()
        inputTurtle.forward(HALF_BOARD_HEIGHT * 2)
        inputTurtle.left(90)

    inputTurtle.color("Black")


# Function to teleport the turtle to a different tile on the board without leaving a trail (Calculates X & Y coordinates provided tile numbers)
# Params:
#   inputRow - row number in numerical value
#   inputColumn - column number in numerical value
def teleportToTile(inputRow, inputColumn, inputTurtle):
    inputTurtle.up()
    # Takes the floored values of the inputted column (to prevent moving to anywhere inside of a tile besides its center) and subtract 0.5 from it to make sure the turtle will teleport to the tile's center
    # Then Calculates the size of each tile on the board by taking half the board's width and dividing it by 4 (there are 4 tiles of each half of the board)
    # Then the two calculated values are multiplied together to get the raw X coordinate of where that tile would be on the board
    # Then the newly calculated value is taken and subtracted from half the width of the board to get the distance from the vertex to that tile
    # Performs the same calculation for the raw Y coordinate & half the board's height to get the raw Y coordinate however the floored input value is unnecessary due to the turtle resting on the horizontal line all the time
    inputTurtle.goto((HALF_BOARD_WIDTH - ((math.floor(inputColumn) - 0.5) * (HALF_BOARD_WIDTH / 4))),
                 (HALF_BOARD_HEIGHT - (math.floor(inputRow) * (HALF_BOARD_HEIGHT / 4))))
    inputTurtle.down()


# Function to calculate the tile requested by the coordinates given (Used to convert raw click data)
# Params:
#   inputX - raw X coordinate in decimal value
#   inputY - raw Y coordinate in decimal value
def coordinatesCalculateTile(inputX, inputY):
    # Calculates row and column based on input
    # Takes the inputted raw Y coordinate and subtracts it from half the board's height to get its current row position on the board
    # Then it calculates the height of each tile by taking half the board's height & dividing it by 4, but adding 1 into it due to grid's boundary being considered otherwise
    # Then divides the two calculated values and absolutes them to make sure the resultant value is a positive value
    # Then floors the resultant value to prevent the calculation returning a value that would be partway in a tile
    # Performs the same calculation using the raw X coordinate & half the board's width to get the column value
    calculatedRow = math.floor(abs(((inputY - HALF_BOARD_HEIGHT) / (HALF_BOARD_HEIGHT / 4))) + 1)
    calculatedColumn = math.floor(abs(((inputX - HALF_BOARD_WIDTH) / (HALF_BOARD_WIDTH / 4))) + 1)

    # Returns the calculated row & column
    return [calculatedRow, calculatedColumn]


# Function to add a piece to the board in the current tile the turtle is located in (To be used with alongside the teleportToTile function)
# Params:
#   playerNumber - the numerical value of the move number
def addPieceToBoard(playerNumber, inputTurtle):
    # Sets the default colour to transparent to prevent accidental fills
    inputTurtle.fillcolor("")
    inputTurtle.color("")

    # Starts the fill method to fill the printed circle
    inputTurtle.begin_fill()

    # If provided 1, fill piece with PLAYER_1_COLOUR
    # If provided 2, fill piece with PLAYER_2_COLOUR
    # If provided 3, fill piece with BOARD_BACKGROUND_COLOUR
    if playerNumber == 1:
        inputTurtle.color("black")
        inputTurtle.fillcolor(PLAYER_1_COLOUR)
    elif playerNumber == 2:
        inputTurtle.color("black")
        inputTurtle.fillcolor(PLAYER_2_COLOUR)
    elif playerNumber == 3:
        inputTurtle.color("black")
        inputTurtle.fillcolor(BOARD_BACKGROUND_COLOUR)

    # Print out circle with radius of 1/16 of board and end fill method
    inputTurtle.circle(abs(HALF_BOARD_WIDTH / 8))
    inputTurtle.end_fill()


# Function to loop through and see if there are any valid moves remaining for either the player or the AI (will be used to determine if the game has ended / turns)
# Params:
#   playerArrayInput - move validity array input for the player
#   aiArrayInput - move validity array input for the AI
def checkForRemainingValidMoves(playerArrayInput, aiArrayInput):
    # Index 0 = number of valid moves for the player
    # Index 1 = number of valid moves for the AI
    validMovesCount = [0, 0]
    for rowCounter in range(9):
        for columnCounter in range(9):
            if playerArrayInput[rowCounter][columnCounter] == 1:
                validMovesCount[0] += 1
            if aiArrayInput[rowCounter][columnCounter] == 1:
                validMovesCount[1] += 1
    return validMovesCount


# Function to run and call other functions when the GUI is clicked
# Params:
#   inputX - raw x coordinate in numerical value
#   inputY - raw y coordinate in numerical value
def graphicalOverlayClicked(inputX, inputY):
    # Calculate tile clicked
    calculatedCoordinates = coordinatesCalculateTile(inputX, inputY)

    # Gets the number of valid moves possible for the player & the AI
    numberOfValidMoves = checkForRemainingValidMoves(copy.deepcopy(backend.findValids(True)), copy.deepcopy(backend.findValids(False)))

    # Stores the current board's status (to keep track of updated pieces)
    oldBoardState = copy.deepcopy(backend.getBoard())

    # Checks to see if the human can perform a move, otherwise skips to the AI, otherwise runs the end game function
    if numberOfValidMoves[0] > 0:
        if calculatedCoordinates[0] <= 8 and calculatedCoordinates[0] > 0 and calculatedCoordinates[1] <= 8 and calculatedCoordinates[1] > 0:
            if (copy.deepcopy(backend.findValids(True))[calculatedCoordinates[0]][calculatedCoordinates[1]]) == 1:
                # Feeds the backend with the user's inputted piece Row & Column values
                backend.playerMove(calculatedCoordinates[0], calculatedCoordinates[1])

                # Updates the board's pieces based on the newly populated board provided from the backend
                updateBoardPieces(backend.getBoard(), pieceTurtle, oldBoardState)

                # Removes the now outdated ghost pieces from the board
                ghostPieceTurtle.clear()

                # Stores the current board's status (to keep track of updated pieces)
                oldBoardState = copy.deepcopy(backend.getBoard())

                # Calls the function that will allow the AI to now perform its turn
                backend.aiMove()

                # Updates the board's pieces based on the newly populated board provided from the backend
                updateBoardPieces(backend.getBoard(), pieceTurtle, oldBoardState)

                # Adds updated ghost pieces onto the board
                addGhostPiecesToBoard(ghostPieceTurtle)

    elif numberOfValidMoves[1] > 0:
        # Removes the now outdated ghost pieces from the board
        ghostPieceTurtle.clear()

        # Calls the function that will allow the AI to now perform its turn
        backend.aiMove()

        # Updates the board's pieces based on the newly populated board provided from the backend
        updateBoardPieces(backend.getBoard(), pieceTurtle, oldBoardState)

        # Adds updated ghost pieces onto the board
        addGhostPiecesToBoard(ghostPieceTurtle)
    elif numberOfValidMoves[0] == 0 and numberOfValidMoves[1] == 0:
        pieceCount = [0, 0]
        for rowCounter in range(1, 9):
            for columnCounter in range(1, 9):
                if backend.getBoard()[rowCounter][columnCounter] == 1:
                    pieceCount[0] += 1
                elif backend.getBoard()[rowCounter][columnCounter] == 2:
                    pieceCount[1] += 1
        if pieceCount[0] > pieceCount[1]:
            endGame("Player Has Won By " + str(pieceCount[0] - pieceCount[1]) + " Pieces!")
        elif pieceCount[1] > pieceCount[0]:
            endGame("AI Has Won By " + str(pieceCount[1] - pieceCount[0]) + " Pieces!")
        elif pieceCount[0] == pieceCount[1]:
            endGame("Draw, No One Has Won!")


# Function to teleport and add the defined colour piece to the board and to the board matrix
# Params:
#   inputRow - row value in numerical value
#   inputColumn - column value coordinate in numerical value
def teleAddPieceToBoard(inputRow, inputColumn, playerNumber, inputTurtle):
    teleportToTile(inputRow, inputColumn, inputTurtle)
    addPieceToBoard(playerNumber, inputTurtle)


# Function to teleport and add the ghost pieces onto the board
def addGhostPiecesToBoard(inputTurtle):
    # Gets the array containing all the valid moves the player can perform
    playerValidMoves = backend.findValids(True)

    # Gets the array containing the current board pieces
    currentBoardState = backend.getBoard()

    # Adds the ghost pieces to the board where there is a valid move opportunity
    for rowCounter in range(9):
        for columnCounter in range(9):
            if playerValidMoves[rowCounter][columnCounter] == 1 and currentBoardState[rowCounter][columnCounter] == 0:
                teleAddPieceToBoard(rowCounter, columnCounter, 3, inputTurtle)


# Function to export the game's current state to a file
def saveGameStateToFile(gameBoard):
    # Initialize a save game file & the save game file writer utility (overwrites any existing file) & specifies that it is to be written to
    saveGameFile = open("Reversi Save Game", "w")

    # Loops through the entire board matrix & writes it to the file
    for rowCounter in range(1, 9):
        for columnCounter in range(1, 9):
            saveGameFile.write(str(gameBoard[rowCounter][columnCounter]))

    # Closes the save game file writer utility
    saveGameFile.close()


# Function to import the game's state from a file
def importGameStateFromFile():
    # Initialize a new list & the save game file reader utility & specifies that it is to be imported from
    saveGameFile = open("Reversi Save Game", "r")
    importedBoard = [[0 for importedMatrixIndex in range(9)] for importedMatrixIndex in range(9)]
    currentIndex = 0
    fileData = saveGameFile.read()

    # Loops through the entire file & imports it into the temp board matrix
    for rowCounter in range(1, 9):
        for columnCounter in range(1, 9):
            importedBoard[rowCounter][columnCounter] = int(fileData[currentIndex:currentIndex + 1])
            currentIndex += 1

    # Closes the save game file reader utility
    saveGameFile.close()

    # Returns backed the fully populated board
    return importedBoard


# Function to rewrite the changed board pieces based on the provided array & comparing + modifying to the original
def updateBoardPieces(inputNewBoardMatrix, inputTurtle, inputOldBoardMatrix = [[0 for i in range(9)] for i in range(9)]):
    # Loops through the entire board matrix, comparing entries & adding in changed pieces
    for rowCounter in range(1, 9):
        for columnCounter in range(1, 9):
            if inputOldBoardMatrix[rowCounter][columnCounter] != inputNewBoardMatrix[rowCounter][columnCounter]:
                teleAddPieceToBoard(rowCounter, columnCounter, int(inputNewBoardMatrix[rowCounter][columnCounter]), inputTurtle)


# Function to handle the end of the game
def endGame(inputEndDialogue):
    userGameRestartPrompt = displayOut.textinput(inputEndDialogue, "Would You Like To Restart? (Yes / No): ")
    if userGameRestartPrompt is None or userGameRestartPrompt.lower() != "yes":
        pass
    elif userGameRestartPrompt.lower() == "yes":
        performInitialSetup()


# Function to perform initial setup for the GUI
def performInitialSetup():
    # Resets The Display Overlay & All The Turtles & The Click Listener & The Piece Data & The Board Matrix
    displayOut.reset()
    boardTurtle.reset()
    pieceTurtle.reset()
    ghostPieceTurtle.reset()
    displayOut.onclick(None)
    blankBoard = [[0 for i in range(9)] for i in range(9)]

    # Populates the board with the initial starting pieces & sends it off to the backend
    blankBoard[4][4] = 1
    blankBoard[4][5] = 2
    blankBoard[5][4] = 2
    blankBoard[5][5] = 1
    backend.writeBoard(blankBoard)

    displayOut.bgcolor(BOARD_BACKGROUND_COLOUR)
    displayOut.title("Reversi By Group 22")
    # Takes Half the width of the board (global constant) and multiplies it by 2 to get the entire board's width
    # Then calculates 1/8th of the board's width and subtracts it from the total width to provide some empty space on the sides
    # Then does the same calculation for the board's height
    displayOut.setup(abs(((HALF_BOARD_WIDTH * 2) + (HALF_BOARD_WIDTH * 0.25))),
                     abs(((HALF_BOARD_HEIGHT * 2) + (HALF_BOARD_HEIGHT * 0.25))))

    # Hides The Turtles & Makes The Animation Speed / Delay Instantaneous
    pieceTurtle.hideturtle()
    pieceTurtle.speed(0)
    boardTurtle.hideturtle()
    boardTurtle.speed(0)
    ghostPieceTurtle.hideturtle()
    ghostPieceTurtle.speed(0)
    displayOut.delay(0)

    # Calls The Functions To Print Out The Intro & Board
    printOutIntro(boardTurtle)
    printOutTable(pieceTurtle)

    # Adds The Default Tiles To The Board
    updateBoardPieces(backend.getBoard(), pieceTurtle)

    # Adds the ghost pieces to the board
    addGhostPiecesToBoard(ghostPieceTurtle)

    # Checks to see if a save file exists & asks the user to import it in & adds the pieces to the board if user specifies
    if os.path.isfile("Reversi Save Game"):
        # Prompts the user for whether or not to import the save game file (Pop Up Box)
        userSaveGamePrompt = displayOut.textinput("Load Save Game", "Save File Found! Load It? (Yes / No): ")
        if userSaveGamePrompt is None or userSaveGamePrompt.lower() != "yes":
            pass
        elif userSaveGamePrompt.lower() == "yes":
            backend.writeBoard(importGameStateFromFile())
            updateBoardPieces(backend.getBoard(), pieceTurtle)
            ghostPieceTurtle.clear()
            addGhostPiecesToBoard(ghostPieceTurtle)

    # Sets The Function That Will Be Called When The User Clicks On The Screen & A Listener For It
    displayOut.onclick(graphicalOverlayClicked)
    displayOut.listen()


# Main function to run the GUI separate from other files
def main():
    # Call initial setup, then wait for user action, then loop though wait for user action
    performInitialSetup()
    displayOut.mainloop()
    saveGameStateToFile(backend.getBoard())


# Calls the main function if the file is called directly
if __name__ == '__main__':
    main()
