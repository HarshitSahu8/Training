'''
i) Write a method Boolean isValidSudoku(int[][]Sudoku)
Returns true if the given Sudoku is correctly arranged otherwise false

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Example : 
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
'''


def isValidSudoku(sudoku):
    hash = dict()
    size = 9
    for row in range(size):
        for column in range(size):
            if sudoku[row][column] in hash:
                return False
            elif sudoku[row][column] != '.':
                hash[sudoku[row][column]] = 0
        hash.clear()
    hash.clear()
    for row in range(size):
        for column in range(size):
            if sudoku[column][row] in hash:
                return False
            elif sudoku[column][row] != '.':
                hash[sudoku[column][row]] = 0
        hash.clear()
    hash.clear()
    return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."], 
         [".", "9", "8", ".", ".", ".", ".", "6", "."], 
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
         [".", "6", ".", ".", ".", ".", "2", "8", "."], 
         [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))
