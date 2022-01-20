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

def isValidSudoku(board):
    size=9
    for i in range(size):
        row={}
        col={}
        block={}
        row_block = 3*(i//3)
        col_block = 3*(i%3)
        for j in range(size):
            if board[i][j]!='.' and board[i][j] in row:
                return False
            row[board[i][j]]=1
            if board[j][i]!='.' and board[j][i] in col:
                return False
            col[board[j][i]]=1
            rb=row_block+(j//3)
            cb=col_block+(j%3)
            if board[rb][cb] in block and board[rb][cb]!='.':
                return False
            block[board[rb][cb]]=1
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