import unittest
import GUI

def SameCheck(fullBoard, emptyBoard):
    for i in range(0,9):
        for j in range(0,9):
            if fullBoard[i][j].value != emptyBoard[i][j].value:
                return False
    return True


# Black box testing for GUI.stringToBoard
# print("GUI.stringToBoard test == " + SameCheck(GUI.stringToBoard("568742913197368254342591687685213479734859162219476538473625891851934726926187345"),
#     Solver.testFullBoard3))
