class Cell:

    def __init__(self,row,column,value):
        self.row = row
        self.column = column
        if value == 0:
            self.value = [1,2,3,4,5,6,7,8,9]
        else:
            self.value = value
        # Dictates the 3x3 square the cell is in
        if row < 3:
            if column < 3:
                self.square = 0
            if 2 < column < 6:
                self.square = 1
            if  5 < column:
                self.square = 2
        if 2 < row < 6:
            if column < 3:
                self.square = 3
            if 2 < column < 6:
                self.square = 4
            if  5 < column:
                self.square = 5
        if 5 < row:
            if column < 3:
                self.square = 6
            if 2 < column < 6:
                self.square = 7
            if  5 < column:
                self.square = 8




class Solver:

    def __init__(self,board):
        self.board = board
        # Rules are added for scale so that things like thermo-sudoku can be added later
        # https://www.gmpuzzles.com/blog/sudoku-rules-and-info/thermo-sudoku-rules-and-info/
        self.rules = "default"

    # Fills in cells that can only have one possible value
    def penFill(self,space):
        for cell in space:
            if isinstance(cell.value,list) and len(cell.value) == 1:
                cell.value = cell.value[0]


    # For each row,col or 3x3 in the board, find the values that are already set, then remove those values
    # from the other cells in that space
    def erase(self,space):
        penValues = []
        for cell in space:
            if isinstance(cell.value,int):
                penValues.append(cell.value)
        for cell in space:
            if isinstance(cell.value,list):
                for i in penValues:
                    try:
                        cell.value.remove(i)
                    except ValueError:
                        pass


# Finds values that belong to only one cell in a space
    def soloPencilCells(self,space):
        pencilValues = [1,2,2,3,4,5,6,7,9]
        pencilCells = []
        # Removes given values of the space from pencilValues
        for cell in space:
            if isinstance(cell.value,int):
                pencilValues.remove(cell.value)
        # This makes iterating through each cell with a list value easier
        for cell in space:
            if isinstance(cell.value,list):
                pencilCells.append(cell)

        # If an element from pencilValues occurs only in one cell from pencilCells, change that pencilCell to
        # the pencilValue element
        for num in pencilValues:
            occur = 0
            for cell in pencilCells:
                try:
                    if num in cell.value:
                        occur = occur + 1
                # Because of the order of the function cycle, a cell which should be penFill'd may be misssed
                # This catches them
                except TypeError:
                    self.penFill([cell])
            if occur == 1:
                cell.value = num
            occur = 0

    # returns True if the board is complete, false otherwise
    def completeCheck(self):
        for row in self.board:
            for cell in row:
                if isinstance(cell.value,list):
                    return False
        return True

    # This function does not get called, but it will be when the code is tidied up / optimised later
    def spaceCycle(self,cellAttribute,nestedFunc):
        space = 1
        while space < 10:
            currentSpace = []
            for row in self.board:
                for cell in row:
                    if cell.cellAttribute == space:
                        currentSpace.append(cell)
                nestedFunc(currentSpace)
            currentSpace = []
            space = space + 1


    # This calls all the functions
    # Not in the right fashion thoguh, these nested loops should to be functions of their own
    # ^ This can wait until later clean up
    # These functions are enough to finish off testBoard
    def functionCycle(self):
        boardCompletion = self.completeCheck()

        timer = 0
        while boardCompletion == False and timer < 75:

            # Checks each row of the board
            for row in self.board:
                self.erase(row)
                self.penFill(row)
                # self.soloPencilCells(row)

            # Checks each column of the board
            col = 1
            while col < 10:
                currentCol = []
                for column in self.board:
                    for cell in column:
                        if cell.column == col:
                            currentCol.append(cell)
                self.erase(currentCol)
                self.penFill(currentCol)
                # self.soloPencilCells(currentCol)
                currentCol = []
                col = col + 1
            col = 0

            # Checks each 3x3 square of the board
            box = 1
            while box < 10:
                currentSquare = []
                for square in self.board:
                    for cell in square:
                        if cell.square == box:
                            currentSquare.append(cell)
                self.erase(currentSquare)
                self.penFill(currentSquare)
                # self.soloPencilCells(currentSquare)
                currentSquare = []
                box = box + 1
            box = 0

            boardCompletion = self.completeCheck()
            timer = timer + 1
            print("cycle complete")
        return self.board


# Testing board quickly made from sudoku app easy difficulty
testFullBoard1 =[
    [Cell(0,0,3),Cell(0,1,7),Cell(0,2,8),   Cell(0,3,6),Cell(0,4,2),Cell(0,5,9),    Cell(0,6,4),Cell(0,7,1),Cell(0,8,5)],
    [Cell(1,0,4),Cell(1,1,2),Cell(1,2,9),   Cell(1,3,8),Cell(1,4,5),Cell(1,5,1),    Cell(1,6,7),Cell(1,7,6),Cell(1,8,3)],
    [Cell(2,0,5),Cell(2,1,6),Cell(2,2,1),   Cell(2,3,7),Cell(2,4,4),Cell(2,5,3),    Cell(2,6,9),Cell(2,7,2),Cell(2,8,8)],

    [Cell(3,0,7),Cell(3,1,4),Cell(3,2,5),   Cell(3,3,1),Cell(3,4,8),Cell(3,5,2),    Cell(3,6,3),Cell(3,7,9),Cell(3,8,6)],
    [Cell(4,0,8),Cell(4,1,3),Cell(4,2,2),   Cell(4,3,9),Cell(4,4,6),Cell(4,5,4),    Cell(4,6,1),Cell(4,7,5),Cell(4,8,7)],
    [Cell(5,0,1),Cell(5,1,9),Cell(5,2,6),   Cell(5,3,5),Cell(5,4,3),Cell(5,5,7),    Cell(5,6,2),Cell(5,7,8),Cell(5,8,4)],

    [Cell(6,0,6),Cell(6,1,1),Cell(6,2,3),   Cell(6,3,2),Cell(6,4,7),Cell(6,5,8),    Cell(6,6,5),Cell(6,7,4),Cell(6,8,9)],
    [Cell(7,0,2),Cell(7,1,5),Cell(7,2,7),   Cell(7,3,4),Cell(7,4,9),Cell(7,5,6),    Cell(7,6,8),Cell(7,7,3),Cell(7,8,1)],
    [Cell(8,0,9),Cell(8,1,8),Cell(8,2,4),   Cell(8,3,3),Cell(8,4,1),Cell(8,5,5),    Cell(8,6,6),Cell(8,7,7),Cell(8,8,2)],
]
testFullBoard2 =[
    [Cell(0,0,6),Cell(0,1,9),Cell(0,2,4),   Cell(0,3,8),Cell(0,4,3),Cell(0,5,2),    Cell(0,6,1),Cell(0,7,5),Cell(0,8,7)],
    [Cell(1,0,8),Cell(1,1,1),Cell(1,2,2),   Cell(1,3,7),Cell(1,4,4),Cell(1,5,5),    Cell(1,6,3),Cell(1,7,9),Cell(1,8,6)],
    [Cell(2,0,3),Cell(2,1,5),Cell(2,2,7),   Cell(2,3,1),Cell(2,4,9),Cell(2,5,6),    Cell(2,6,2),Cell(2,7,8),Cell(2,8,4)],

    [Cell(3,0,1),Cell(3,1,3),Cell(3,2,5),   Cell(3,3,9),Cell(3,4,8),Cell(3,5,4),    Cell(3,6,6),Cell(3,7,7),Cell(3,8,2)],
    [Cell(4,0,7),Cell(4,1,2),Cell(4,2,8),   Cell(4,3,6),Cell(4,4,1),Cell(4,5,3),    Cell(4,6,5),Cell(4,7,4),Cell(4,8,9)],
    [Cell(5,0,9),Cell(5,1,4),Cell(5,2,6),   Cell(5,3,2),Cell(5,4,5),Cell(5,5,7),    Cell(5,6,8),Cell(5,7,3),Cell(5,8,1)],

    [Cell(6,0,4),Cell(6,1,7),Cell(6,2,3),   Cell(6,3,5),Cell(6,4,6),Cell(6,5,1),    Cell(6,6,9),Cell(6,7,2),Cell(6,8,8)],
    [Cell(7,0,5),Cell(7,1,8),Cell(7,2,1),   Cell(7,3,4),Cell(7,4,2),Cell(7,5,9),    Cell(7,6,7),Cell(7,7,6),Cell(7,8,3)],
    [Cell(8,0,2),Cell(8,1,6),Cell(8,2,9),   Cell(8,3,3),Cell(8,4,7),Cell(8,5,8),    Cell(8,6,4),Cell(8,7,1),Cell(8,8,5)],
]
testFullBoard3 =[
    [Cell(0,0,5),Cell(0,1,6),Cell(0,2,8),   Cell(0,3,7),Cell(0,4,4),Cell(0,5,2),    Cell(0,6,9),Cell(0,7,1),Cell(0,8,3)],
    [Cell(1,0,1),Cell(1,1,9),Cell(1,2,7),   Cell(1,3,3),Cell(1,4,6),Cell(1,5,8),    Cell(1,6,2),Cell(1,7,5),Cell(1,8,4)],
    [Cell(2,0,3),Cell(2,1,4),Cell(2,2,2),   Cell(2,3,5),Cell(2,4,9),Cell(2,5,1),    Cell(2,6,6),Cell(2,7,8),Cell(2,8,7)],

    [Cell(3,0,6),Cell(3,1,8),Cell(3,2,5),   Cell(3,3,2),Cell(3,4,1),Cell(3,5,3),    Cell(3,6,4),Cell(3,7,7),Cell(3,8,9)],
    [Cell(4,0,7),Cell(4,1,3),Cell(4,2,4),   Cell(4,3,8),Cell(4,4,5),Cell(4,5,9),    Cell(4,6,1),Cell(4,7,6),Cell(4,8,2)],
    [Cell(5,0,2),Cell(5,1,1),Cell(5,2,9),   Cell(5,3,4),Cell(5,4,7),Cell(5,5,6),    Cell(5,6,5),Cell(5,7,3),Cell(5,8,8)],

    [Cell(6,0,4),Cell(6,1,7),Cell(6,2,3),   Cell(6,3,6),Cell(6,4,2),Cell(6,5,5),    Cell(6,6,8),Cell(6,7,9),Cell(6,8,1)],
    [Cell(7,0,8),Cell(7,1,5),Cell(7,2,1),   Cell(7,3,9),Cell(7,4,3),Cell(7,5,4),    Cell(7,6,7),Cell(7,7,2),Cell(7,8,6)],
    [Cell(8,0,9),Cell(8,1,2),Cell(8,2,6),   Cell(8,3,1),Cell(8,4,8),Cell(8,5,7),    Cell(8,6,3),Cell(8,7,4),Cell(8,8,5)],
]

testBoard1 =[
    [Cell(0,0,3),Cell(0,1,7),Cell(0,2,8),   Cell(0,3,6),Cell(0,4,2),Cell(0,5,9),    Cell(0,6,4),Cell(0,7,0),Cell(0,8,5)],
    [Cell(1,0,0),Cell(1,1,0),Cell(1,2,9),   Cell(1,3,0),Cell(1,4,0),Cell(1,5,1),    Cell(1,6,7),Cell(1,7,6),Cell(1,8,0)],
    [Cell(2,0,0),Cell(2,1,0),Cell(2,2,0),   Cell(2,3,0),Cell(2,4,4),Cell(2,5,0),    Cell(2,6,0),Cell(2,7,0),Cell(2,8,8)],

    [Cell(3,0,0),Cell(3,1,0),Cell(3,2,0),   Cell(3,3,1),Cell(3,4,8),Cell(3,5,0),    Cell(3,6,0),Cell(3,7,9),Cell(3,8,0)],
    [Cell(4,0,0),Cell(4,1,0),Cell(4,2,2),   Cell(4,3,0),Cell(4,4,0),Cell(4,5,4),    Cell(4,6,0),Cell(4,7,5),Cell(4,8,7)],
    [Cell(5,0,0),Cell(5,1,0),Cell(5,2,6),   Cell(5,3,5),Cell(5,4,3),Cell(5,5,7),    Cell(5,6,2),Cell(5,7,0),Cell(5,8,0)],

    [Cell(6,0,0),Cell(6,1,1),Cell(6,2,0),   Cell(6,3,2),Cell(6,4,0),Cell(6,5,0),    Cell(6,6,5),Cell(6,7,0),Cell(6,8,0)],
    [Cell(7,0,0),Cell(7,1,5),Cell(7,2,7),   Cell(7,3,0),Cell(7,4,0),Cell(7,5,0),    Cell(7,6,0),Cell(7,7,0),Cell(7,8,1)],
    [Cell(8,0,9),Cell(8,1,0),Cell(8,2,4),   Cell(8,3,3),Cell(8,4,1),Cell(8,5,0),    Cell(8,6,6),Cell(8,7,7),Cell(8,8,0)],
]
testBoard2 =[
    [Cell(0,0,0),Cell(0,1,9),Cell(0,2,4),   Cell(0,3,0),Cell(0,4,3),Cell(0,5,0),    Cell(0,6,1),Cell(0,7,0),Cell(0,8,0)],
    [Cell(1,0,8),Cell(1,1,1),Cell(1,2,2),   Cell(1,3,7),Cell(1,4,0),Cell(1,5,0),    Cell(1,6,0),Cell(1,7,9),Cell(1,8,6)],
    [Cell(2,0,3),Cell(2,1,0),Cell(2,2,0),   Cell(2,3,1),Cell(2,4,9),Cell(2,5,0),    Cell(2,6,0),Cell(2,7,0),Cell(2,8,0)],

    [Cell(3,0,0),Cell(3,1,3),Cell(3,2,0),   Cell(3,3,9),Cell(3,4,0),Cell(3,5,4),    Cell(3,6,6),Cell(3,7,0),Cell(3,8,0)],
    [Cell(4,0,0),Cell(4,1,0),Cell(4,2,8),   Cell(4,3,6),Cell(4,4,1),Cell(4,5,3),    Cell(4,6,0),Cell(4,7,4),Cell(4,8,9)],
    [Cell(5,0,0),Cell(5,1,0),Cell(5,2,6),   Cell(5,3,2),Cell(5,4,0),Cell(5,5,0),    Cell(5,6,0),Cell(5,7,0),Cell(5,8,1)],

    [Cell(6,0,4),Cell(6,1,0),Cell(6,2,3),   Cell(6,3,5),Cell(6,4,0),Cell(6,5,0),    Cell(6,6,0),Cell(6,7,0),Cell(6,8,8)],
    [Cell(7,0,5),Cell(7,1,0),Cell(7,2,0),   Cell(7,3,0),Cell(7,4,2),Cell(7,5,0),    Cell(7,6,7),Cell(7,7,0),Cell(7,8,0)],
    [Cell(8,0,0),Cell(8,1,6),Cell(8,2,0),   Cell(8,3,0),Cell(8,4,0),Cell(8,5,8),    Cell(8,6,4),Cell(8,7,1),Cell(8,8,5)],
]
testBoard3 =[
    [Cell(0,0,5),Cell(0,1,6),Cell(0,2,0),   Cell(0,3,7),Cell(0,4,0),Cell(0,5,0),    Cell(0,6,0),Cell(0,7,0),Cell(0,8,3)],
    [Cell(1,0,0),Cell(1,1,9),Cell(1,2,0),   Cell(1,3,0),Cell(1,4,6),Cell(1,5,0),    Cell(1,6,0),Cell(1,7,0),Cell(1,8,0)],
    [Cell(2,0,3),Cell(2,1,4),Cell(2,2,0),   Cell(2,3,5),Cell(2,4,0),Cell(2,5,1),    Cell(2,6,6),Cell(2,7,0),Cell(2,8,0)],

    [Cell(3,0,6),Cell(3,1,8),Cell(3,2,0),   Cell(3,3,0),Cell(3,4,1),Cell(3,5,0),    Cell(3,6,4),Cell(3,7,7),Cell(3,8,0)],
    [Cell(4,0,0),Cell(4,1,0),Cell(4,2,0),   Cell(4,3,0),Cell(4,4,5),Cell(4,5,9),    Cell(4,6,0),Cell(4,7,6),Cell(4,8,0)],
    [Cell(5,0,2),Cell(5,1,1),Cell(5,2,0),   Cell(5,3,0),Cell(5,4,0),Cell(5,5,0),    Cell(5,6,5),Cell(5,7,0),Cell(5,8,0)],

    [Cell(6,0,0),Cell(6,1,7),Cell(6,2,0),   Cell(6,3,0),Cell(6,4,2),Cell(6,5,5),    Cell(6,6,8),Cell(6,7,0),Cell(6,8,1)],
    [Cell(7,0,0),Cell(7,1,0),Cell(7,2,0),   Cell(7,3,9),Cell(7,4,0),Cell(7,5,0),    Cell(7,6,0),Cell(7,7,0),Cell(7,8,0)],
    [Cell(8,0,0),Cell(8,1,0),Cell(8,2,0),   Cell(8,3,0),Cell(8,4,0),Cell(8,5,0),    Cell(8,6,3),Cell(8,7,4),Cell(8,8,5)],
]

currentBoard = Solver(testBoard3)

