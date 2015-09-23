"""
2015/09/23

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
The Program Will Print Out The Reversi Table Using Turtle Graphics & Prompt The User For An Input Piece Coordinate & Echo It Back Out
"""

# Imports In The Turtle Graphics Module
import turtle

# Initialize Variables
boardTopLeftX = -250
boardTopLeftY = 250
placePieceX = 0
placePieceY = 0

# Initialize The Display Out & The First Turtle
displayOut = turtle.Screen()
turtle1 = turtle.Turtle()

# Hides The Turtle Pointer
turtle1.hideturtle()

# Sets The Drawing Speed Of The Turtle
turtle1.speed(10)

# For Loop To Teleport The Turtle To Coordinates & Print The Reversi Table
for indexCounter in range(0, 9):
    # Lifts Up The Turtle & Prevents It From Leaving A Trail
    turtle1.up()
    # Teleports The Turtle To The Left Hand Side Of The Next Row
    turtle1.goto(boardTopLeftX, boardTopLeftY - indexCounter * boardTopLeftY / 4)
    # Lowers The Turtle & Allows It To Leave A Trail Again
    turtle1.down()
    # Prints Out The Row's Line
    turtle1.forward(boardTopLeftX * -2)

    # Turns The Turtle Right To Print Out A Vertical Line
    turtle1.right(90)
    # Lifts Up The Turtle & Prevents It From Leaving A Trail
    turtle1.up()
    # Teleports The Turtle To The Top Of The Next Column
    turtle1.goto(boardTopLeftX - indexCounter * boardTopLeftX / 4, boardTopLeftY)
    # Lowers The Turtle & Allows It To Leave A Trail Again
    turtle1.down()
    # Prints Out The Row's Line
    turtle1.forward(boardTopLeftY * 2)
    # Turns The Turtle Back Left To Print Out The Horizontal Line
    turtle1.left(90)

print("Welcome to" + "\n" + 
"""╦═╗┌─┐┬  ┬┌─┐┬─┐┌─┐┬
╠╦╝├┤ └┐┌┘├┤ ├┬┘└─┐│
╩╚═└─┘ └┘ └─┘┴└─└─┘┴""" + "\n" + 
"In this game you will be able to..." + "\n" +
"""╔╦╗┬ ┬┌─┐┌─┐  ╔═╗┌─┐┌┬┐┌─┐┌┬┐┬ ┬┬┌┐┌┌─┐  
 ║ └┬┘├─┘├┤   ╚═╗│ ││││├┤  │ ├─┤│││││ ┬  
 ╩  ┴ ┴  └─┘  ╚═╝└─┘┴ ┴└─┘ ┴ ┴ ┴┴┘└┘└─┘ 
"""+ "\n" +
"You will eventually be able to click on the tile where you want to play your piece, but for now, please input coordinates. The point of the game is as follows:"+ "\n" +
"""╔═╗┌─┐┌┬┐  ┌─┐┌─┐  ┌┬┐┌─┐┌┐┌┬ ┬  ┌─┐┬┌─┐┌─┐┌─┐┌─┐
║ ╦├┤  │   ├─┤└─┐  │││├─┤│││└┬┘  ├─┘│├┤ │  ├┤ └─┐
╚═╝└─┘ ┴   ┴ ┴└─┘  ┴ ┴┴ ┴┘└┘ ┴   ┴  ┴└─┘└─┘└─┘└─┘
┌─┐┌─┐  ┌─┐┌─┐┌─┐┌─┐┬┌┐ ┬  ┌─┐                   
├─┤└─┐  ├─┘│ │└─┐└─┐│├┴┐│  ├┤                    
┴ ┴└─┘  ┴  └─┘└─┘└─┘┴└─┘┴─┘└─┘                   
┬┌┐┌  ┬ ┬┌─┐┬ ┬┬─┐  ┌─┐┌─┐┬  ┌─┐┬ ┬┬─┐           
││││  └┬┘│ ││ │├┬┘  │  │ ││  │ ││ │├┬┘           
┴┘└┘   ┴ └─┘└─┘┴└─  └─┘└─┘┴─┘└─┘└─┘┴└─  
""")

# Endless While Loop To Handle The User's Inputted Move
while 1 == 1:
    # Prompts The User For Their Move's Location & Stores It In Variables
    placePieceX = input("\nRow You Would Like To Place A Piece In: ")
    placePieceY = input("Column You Would Like To Place A Piece In: ")
    # Echoes Out The User's Entered Coordinates
    print("Piece At Row:", placePieceX, " Column:", placePieceY)

# Closes The Program If The GUI Overlay Is Clicked
displayOut.exitonclick()
