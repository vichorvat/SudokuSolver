import Solver
import GUI
from tkinter import *


root = Tk()
root.title("SudokuSolver")


Board = Solver.currentBoard.functionCycle()
GUI.boardLoad(Board)
root.mainloop()