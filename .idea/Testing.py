

def SameCheck(fullBoard, emptyBoard):
    for i in range(0,9):
        for j in range(0,9):
            if fullBoard[i][j].value != emptyBoard[i][j].value:
                return False
    return True