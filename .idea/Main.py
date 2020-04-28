class Cell:
    def __init__(self,row,column,value):
        self.row = row
        self.column = column
        if value == 0:
            self.value = [1,2,3,4,5,6,7,8,9]
        else:
            self.value = value



# Testing board quickly made from sudoku app easy difficulty
testFullBoard =[
    [Cell(1,1,7),Cell(1,2,3),Cell(1,3,9),Cell(1,4,5), Cell(1,5,1),Cell(1,6,8), Cell(1,7,4),Cell(1,8,2),Cell(1,9,6)],
    [Cell(2,1,8),Cell(2,2,2),Cell(2,3,4),Cell(2,4,6), Cell(2,5,7),Cell(2,6,9), Cell(2,7,5),Cell(2,8,3),Cell(2,9,1)],
    [Cell(3,1,5),Cell(3,2,6),Cell(3,3,1),Cell(3,4,3), Cell(3,5,2),Cell(3,6,4), Cell(3,7,8),Cell(3,8,9),Cell(3,9,7)],

    [Cell(4,1,4),Cell(4,2,9),Cell(4,3,8),Cell(4,4,7), Cell(4,5,3),Cell(4,6,6), Cell(4,7,1),Cell(4,8,5),Cell(4,9,2)],
    [Cell(5,1,3),Cell(5,2,5),Cell(5,3,6),Cell(5,4,2), Cell(5,5,4),Cell(5,6,1), Cell(5,7,7),Cell(5,8,8),Cell(5,9,9)],
    [Cell(6,1,1),Cell(6,2,7),Cell(6,3,2),Cell(6,4,9), Cell(6,5,8),Cell(6,6,5), Cell(6,7,6),Cell(6,8,4),Cell(6,9,3)],

    [Cell(7,1,2),Cell(7,2,1),Cell(7,3,5),Cell(7,4,4), Cell(7,5,6),Cell(7,6,3), Cell(7,7,9),Cell(7,8,7),Cell(7,9,8)],
    [Cell(8,1,6),Cell(8,2,4),Cell(8,3,3),Cell(8,4,8), Cell(8,5,9),Cell(8,6,7), Cell(8,7,2),Cell(8,8,1),Cell(8,9,5)],
    [Cell(9,1,9),Cell(9,2,8),Cell(9,3,7),Cell(9,4,1), Cell(9,5,5),Cell(9,6,2), Cell(9,7,3),Cell(9,8,6),Cell(9,9,4)],
]

testBoard =[
    [Cell(1,1,0),Cell(1,2,3),Cell(1,3,9),Cell(1,4,0),Cell(1,5,1),Cell(1,6,0),Cell(1,7,4),Cell(1,8,0),Cell(1,9,0)],
    [Cell(2,1,0),Cell(2,2,0),Cell(2,3,4),Cell(2,4,6),Cell(2,5,0),Cell(2,6,9),Cell(2,7,0),Cell(2,8,0),Cell(2,9,1)],
    [Cell(3,1,5),Cell(3,2,0),Cell(3,3,0),Cell(3,4,3),Cell(3,5,2),Cell(3,6,0),Cell(3,7,0),Cell(3,8,9),Cell(3,9,0)],
    [Cell(4,1,4),Cell(4,2,0),Cell(4,3,0),Cell(4,4,0),Cell(4,5,0),Cell(4,6,0),Cell(4,7,0),Cell(4,8,5),Cell(4,9,2)],
    [Cell(5,1,0),Cell(5,2,0),Cell(5,3,0),Cell(5,4,2),Cell(5,5,4),Cell(5,6,1),Cell(5,7,0),Cell(5,8,0),Cell(5,9,0)],
    [Cell(6,1,1),Cell(6,2,7),Cell(6,3,0),Cell(6,4,0),Cell(6,5,0),Cell(6,6,0),Cell(6,7,0),Cell(6,8,0),Cell(6,9,3)],
    [Cell(7,1,0),Cell(7,2,1),Cell(7,3,0),Cell(7,4,0),Cell(7,5,6),Cell(7,6,3),Cell(7,7,0),Cell(7,8,0),Cell(7,9,8)],
    [Cell(8,1,6),Cell(8,2,0),Cell(8,3,0),Cell(8,4,8),Cell(8,5,0),Cell(8,6,7),Cell(8,7,2),Cell(8,8,0),Cell(8,9,0)],
    [Cell(9,1,0),Cell(9,2,0),Cell(9,3,7),Cell(9,4,0),Cell(9,5,5),Cell(9,6,0),Cell(9,7,3),Cell(9,8,6),Cell(9,9,0)],
]


# Combs through a row to find and fill an empty cell
def oneCellFill(row):
    for cell in row:
        if cell == " ":
            penFill = cellFillHelper(row)
            row[row.index(" ")] = penFill[0]

# Checks to see if there is only one empty cell in a row,column or 3x3
def oneCellCheck(row):
    emptyCount = 0
    for number in row:
        if number == " ":
            emptyCount = emptyCount + 1
    if emptyCount == 1:
        return True
    else:
        return False

# Iterates through numbers 1-9 and returns the missing values for empty cells
def cellFillHelper(row):
    # This lets numberList remain for future checks
    tempNumberList = [1,2,3,4,5,6,7,8,9]
    for cell in row:
        for number in tempNumberList:
            if number == cell:
                tempNumberList.remove(number)
    return(tempNumberList)


# # Searches the sudoku for missing cells
def emptyCellSearch(board):
    # Check rows
    for row in board:
        if oneCellCheck(row):
            oneCellFill(row)
    # Check columns
    colBoard = rowToCol(board)
    for col in colBoard:
        if oneCellCheck(col):
            oneCellFill(col)


# Converts from board of rows, to board of columns
def rowToCol(board):
    print(board)
    colBoard = []
    column = []
    for x in range((len(board[0]))):
        for y in board:
            # print("y: "+str(y))
            # print("x: "+str(x))
            column.append(y[x])
        colBoard.append(column)
        column = []
    print(colBoard)


# emptyCellSearch(testBoard)

rowToCol(testFullBoard)
