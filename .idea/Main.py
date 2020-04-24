
# Testing board quickly made from sudoku app easy difficulty
testFullBoard =[
    [5,3,1,6,2,7,9,8,4],
    [6,4,9,8,1,3,2,5,7],
    [8,2,7,5,9,4,6,1,3],
    [4,9,6,1,7,5,8,3,2],
    [2,1,8,3,6,9,7,4,5],
    [7,5,3,2,4,8,1,9,6],
    [9,6,2,4,5,1,3,7,8],
    [1,8,5,7,3,6,4,2,9],
    [3,7,4,9,8,2,5,6,1]
    ]
testBoard =[
    [" ",3,1,6,2,7,9,8,4],
    [6,4,9,8,1,3,2,5,7],
    [8,2,7,5,9,4,6,1,3],
    [4,9,6,1,7,5,8,3,2],
    [2,1,8,3,6,9,7,4,5],
    [7,5,3,2,4,8,1,9,6],
    [9,6,2,4,5,1,3,7,8],
    [1,8,5,7,3,6,4,2,9],
    [3,7,4,9,8,2,5,6,1]
]
# just to make checking easier
numberList = [1,2,3,4,5,6,7,8,9]



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
