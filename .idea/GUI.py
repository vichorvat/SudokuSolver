import Main

def boardToString(board):
    output = ""
    counter = 0
    for row in board:
        if len(output) > 0:
            print(boardToStringHelper(output))
            counter = counter + 1
        # for line breaks
        if counter == 3:
            print(" ")
            counter = 0
        output = ""
        for cell in row:
            # Checks to see if the cell has a value
            if cell.value != [1,2,3,4,5,6,7,8,9]:
                output = output + str(cell.value)
            else:
                output = output + "0" # completely arbirtrary square ascii value
    print(boardToStringHelper(output))

# This helps by dividing up each row and splicing it for the spacing
def boardToStringHelper(row):
    firstThird = row[0:3]
    secondThird = row[3:6]
    finalThird = row[6:9]
    output = firstThird + " " + secondThird + " " + finalThird
    return output


boardToString(Main.testBoard)
boardToString(Main.firstSudoku.functionCycle())

