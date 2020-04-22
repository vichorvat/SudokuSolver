
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
    [5,3,1,6,2,7,9,8,4],
    [6,4,9,8,1,3,2,5,7],
    [8,2,7,5,9,4,6,1,3],
    [4,9,6,1,7,5,8,3,2],
    [2,1,8,3," ",9,7,4,5],
    [7,5,3,2,4,8,1,9,6],
    [9,6,2,4,5,1,3,7,8],
    [1,8,5,7,3,6,4,2,9],
    [3,7,4,9,8,2,5,6,1]
]
# just to make checking easier
numberList = [1,2,3,4,5,6,7,8,9]


# Combs through a row to find and fill an empty cell
def oneCellRowSearch(row):
    for cell in row:
        if cell == " ":
            penFill = missingCells(row)
            row[row.index(" ")] = penFill[0]


# Iterates through numbers 1-9 and returns the missing values for empty cells
def missingCells(row):
    # This lets numberList remain for future checks
    tempNumberList = numberList
    for cell in row:
        for number in tempNumberList:
            if number == cell:
                tempNumberList.remove(number)
    return(tempNumberList)


oneCellRowSearch([2,1,8,3," ",9,7,4,5])