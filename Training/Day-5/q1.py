'''
Prints array elements clock wise and anti-clockwise alternatively.
Input : 
 1 2 3
 4 5 6
 7 8 9
Output :
1 2 3 6 9 8 7 4 5
3 2 1 4 7 8 9 6 5
'''
def rotateMatrix(mat):
    for x in range(0, int(N / 2)):
        for y in range(x, N-x-1):
            temp = mat[x][y]
            mat[x][y] = mat[y][N-1-x]
            mat[y][N-1-x] = mat[N-1-x][N-1-y]
            mat[N-1-x][N-1-y] = mat[N-1-y][x]
            mat[N-1-y][x] = temp

def clockwise(matrix,eri,eci): #eri-ending row index eci-ending column index
    sri = 0
    sci = 0
    while (sri < eri and sci < eci):
        for i in range(sci, eci):
            print(matrix[sri][i], end=" ")
        sri += 1
        for i in range(sri, eri):
            print(matrix[i][eci - 1], end=" ")
        eci -= 1
        if (sri < eri):
            for i in range(eci - 1, (sci - 1), -1):
                print(matrix[eri - 1][i], end=" ")
            eri -= 1
        if (sci < eci):
            for i in range(eri - 1, sri - 1, -1):
                print(matrix[i][sci], end=" ")
            sci += 1
    print()
def anticlockwise(matrix,row,col):
    sri = 0; sci = 0
    count = 0
    total = row * col
    while (sri < row and sci < col) :
        if (count == total) :
            break
        for i in range(sri, row) :
            print(matrix[i][sci], end = " ")
            count += 1
        sci += 1
        if (count == total) :
            break
        for i in range (sci, col) :
            print( matrix[row - 1][i], end = " ")
            count += 1
        row -= 1
        if (count == total) :
            break
        if (sri < row) :
            for i in range(row - 1, sri - 1, -1) :
                print(matrix[i][col - 1], end = " ")
                count += 1
            col -= 1
        if (count == total) :
            break
        if (sci < col) :
            for i in range(col - 1, sci - 1, -1) :
                print( matrix[sri][i], end = " ")
                count += 1
                 
            sri += 1
    
    

# row=int(input('Enter no. of rows: '))
# col=int(input('Enter no. of column: '))
# matrix=[[int(input()) for i in range(row)]for j in range(col)]


# for i in range(row):
#     for j in range(col):
#         print(matrix[i][j], end=' ')
#     print()

clockwise([[1,2,3],[4,5,6],[7,8,9]],3,3)
anticlockwise([[1,2,3],[4,5,6],[7,8,9]],3,3)