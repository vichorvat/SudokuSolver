import Solver
import GUI
from tkinter import *


root = Tk()
root.title("SudokuSolver")


Board = Solver.currentBoard.functionCycle()
# Board = Solver.testFullBoard1
GUI.boardLoad(Board)

# stringBoard = GUI.stringToBoard("568742913197368254342591687685213479734859162219476538473625891851934726926187345",Solver.emptyBoard)
# GUI.boardLoad(GUI.stringToBoard("568742913197368254342591687685213479734859162219476538473625891851934726926187345",Solver.emptyBoard))

root.mainloop()