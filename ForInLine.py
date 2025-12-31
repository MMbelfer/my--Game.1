# class Board:
#     def __init__(self):

#         self.Cells = [
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0]]


import random

print("Hi,\nWolcam to-the-Game!")
print("-------------------")

LainLetters = ["A", "B", "C", "D", "E", "F", "G"]

gameBoard = [
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""],
    ["", "", "", "", "", "", ""]
]

rows = 6
cols = 7

def printGameBorard():
    print("\n    A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " | ", end="")
        for y in range(cols):
            if(gameBoard[x][y] == "🔵"):
                print("", gameBoard[x][y], end="  | ")
            elif(gameBoard[x][y] == "🔴"):
                print("", gameBoard[x][y], end="  | ")
            else:
                print(" ", gameBoard[x][y], end="   | ")
        print("\n   +----+----+----+----+----+----+----+")
        
printGameBorard()