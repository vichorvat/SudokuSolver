import Main

def boardToString(board):
    threeCell = ""
    for i in board:
        print("row")
        if (len(threeCell) % 3 == 0):
            print(threeCell)
            threeCell = ""
        for j in i:

            threeCell = threeCell + str(j)
            # print(j)





print(Main.Board)

boardToString(Main.Board)