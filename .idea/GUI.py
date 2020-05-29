import Main
import Testing
from tkinter import *



root = Tk()
root.title("SudokuSolver")
def boardLoad(board):
    for row in board:
        for cell in row:
            label = Label(root, text = cell.value)
            label.grid(row = cell.row, column = cell.column)


# GUIBoard = Main.board.functionCycle()
GUIBoard = Main.board.functionCycle()




boardLoad(GUIBoard)


root.mainloop()