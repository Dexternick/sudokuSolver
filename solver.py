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
    for i in range(9):
        if sudoku[rowNumber][i] == toInsert:
            return False
    return True


def column_checker(sudoku, columnNumber, toInsert):
    for i in range(9):
        if sudoku[i][columnNumber] == toInsert:
            return False
    return True


def box_checker(sudoku, boxRow, boxColumn, toInsert):
    for i in range(3):
        for j in range(3):
            if sudoku[boxRow+i][boxColumn+j] == toInsert:
                return False
            print(sudoku[boxRow+i][boxColumn+j])
    print("ok")
    return True

#def sudoku_solver(sudoku, row, column):

