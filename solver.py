puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def row_checker(sudoku, rowNumber, toInsert):
    return False

def column_checker(sudoku, columnNumber, toInsert):
    return False

def box_checker(sudoku, boxNumber, toInsert):
    return False

def sudoku_solver(sudoku, N):
    if N is 0:
        return True
    for i in range(1, N+1):
        for j in range(1, N+1):
            if

