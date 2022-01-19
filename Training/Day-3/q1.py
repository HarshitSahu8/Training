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
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] in hash:
                return False
            elif sudoku[i][j] != '.':
                hash[sudoku[i][j]] = 0
        hash.clear()
    hash.clear()
    for i in range(9):
        for j in range(9):
            if sudoku[j][i] in hash:
                return False
            elif sudoku[j][i] != '.':
                hash[sudoku[j][i]] = 0
        hash.clear()
    hash.clear()
    return True


board = board = [["8", "3", ".", ".", "7", ".", ".", ".", "."], 
                 ["6", ".", ".", "1", "9", "5", ".", ".", "."], 
                 [".", "9", "8", ".", ".", ".", ".", "6", "."], 
                 ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
                 ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
                 [".", "6", ".", ".", ".", ".", "2", "8", "."], 
                 [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))
