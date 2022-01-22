'''
.Given an m x n 2D binary grid grid which represents a map of '1's (land) 
and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent 
lands horizontally or vertically. You may assume all four edges of 
the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''
def dfs(matrix,x,y,r,c):
    if x<0 or x>=r or y<0 or y>=c or matrix[x][y]!='1':
        return
    matrix[x][y]='2'
    dfs(matrix,x+1,y,r,c)
    dfs(matrix,x,y+1,r,c)
    dfs(matrix,x-1,y,r,c)
    dfs(matrix,x,y-1,r,c)
    
def island(grid):
    r=len(grid)
    if r==0:
        return 0
    c=len(grid[0])
    count=0
    for i in range(r):
        for j in range(c):
            if grid[i][j]=='1':
                dfs(grid,i,j,r,c)
                count+=1

    return count
    

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(island(grid))
