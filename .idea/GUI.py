import Main
from tkinter import *



root = Tk()
root.title("SudokuSolver")
def boardLoad():
    for row in Main.testBoard:
        for cell in row:
            print(cell.value)
            label = Label(root, text = cell.value)
            label.grid(row = cell.row, column = cell.column)


boardLoad()
root.mainloop()


