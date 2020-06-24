from tkinter import *



root = Tk()
root.title("SudokuSolver")

def boardLoad(board):
    for row in board:
        for cell in row:
            if cell.square == 1:
                label = Label(root, text = cell.value)
                label.grid(row = cell.row, column = cell.column)
            if cell.square == 2:
                label = Label(root, text = cell.value)
                label.grid(row = cell.row, column = cell.column + 1)
            if cell.square == 3:
                label = Label(root, text = cell.value)
                label.grid(row = cell.row, column = cell.column + 2)

            if cell.square == 4:
                label = Label(root, text = cell.value)
                label.grid(row = cell.row + 1, column = cell.column)
            if cell.square == 5:
                label = Label(root, text = cell.value)
                label.grid(row = cell.row + 1, column = cell.column + 1)
            if cell.square == 6:
                label = Label(root, text = cell.value)
                label.grid(row = cell.row + 1, column = cell.column + 2)

            if cell.square == 7:
                label = Label(root, text = cell.value)
                label.grid(row = cell.row + 2, column = cell.column)
            if cell.square == 8:
                label = Label(root, text = cell.value)
                label.grid(row = cell.row + 2, column = cell.column + 1)
            if cell.square == 9:
                label = Label(root, text = cell.value)
                label.grid(row = cell.row + 2, column = cell.column + 2)

            # This prints out each column divider
            label = Label(root, text = "|")
            label.grid(row = cell.row, column = 4)
            label = Label(root, text = "|")
            label.grid(row = cell.row, column = 8)
            # This prints out each row divider
            label = Label(root, text = "=")
            label.grid(row = 4, column = cell.column)
            label = Label(root, text = "=")
            label.grid(row = 8, column = cell.column)
    # The column and row dividers fall 2 cells short, this for loop fixes this issue
    for i in range (1,3):
        label = Label(root, text = "|")
        label.grid(row = 9 + i, column = 4)
        label = Label(root, text = "|")
        label.grid(row = 9 + i, column = 8)
        label = Label(root, text = "=")
        label.grid(row = 4, column = 9 + i)
        label = Label(root, text = "=")
        label.grid(row = 8, column = 9 + i)

# This will be integrated later as a helper function to help users enter in their own boards for solving
def stringToBoard(str,board):

    # ranges defined by row and row.length respectively
    for i in range(0,9):
        for j in range(0,9):
            board[i][j].value = str[i*9 + j]
            # print(str[i*9 + j])



# stringToBoard("568742913197368254342591687685213479734859162219476538473625891851934726926187345")
# boardLoad(emptyBoard)