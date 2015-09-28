"""
2015/XX/XX

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
This part of the game is in charge of simply being called by the GUI.py to print out ASCII (Due to Windows overwriting UTF-8 ASCII the need for this file exists)
"""


def printOutASCII():
    print("Welcome to" + "\n" +
          """╦═╗┌─┐┬  ┬┌─┐┬─┐┌─┐┬
          ╠╦╝├┤ └┐┌┘├┤ ├┬┘└─┐│
          ╩╚═└─┘ └┘ └─┘┴└─└─┘┴""" + "\n" +
          "In this game you will be able to..." + "\n" +
          """╔╦╗┬ ┬┌─┐┌─┐  ╔═╗┌─┐┌┬┐┌─┐┌┬┐┬ ┬┬┌┐┌┌─┐
           ║ └┬┘├─┘├┤   ╚═╗│ ││││├┤  │ ├─┤│││││ ┬
           ╩  ┴ ┴  └─┘  ╚═╝└─┘┴ ┴└─┘ ┴ ┴ ┴┴┘└┘└─┘
          """ + "\n" +
          "You will eventually be able to click on the tile where you want to play your piece, but for now, please input coordinates. The point of the game is as follows:" + "\n" +
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
