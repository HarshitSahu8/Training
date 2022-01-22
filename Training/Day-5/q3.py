def find(matrix,target):
    row=len(matrix)
    for i in range(row):
        col=len(matrix[i])
        last=matrix[i][col-1]
        if target<last:
            for j in range(col):
                if matrix[i][j]==target:
                    return True
    return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(find(matrix,target))
