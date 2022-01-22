def rotateMatrix(arr,n):
    for j in range(n) :
        for i in range(n - 1, -1, -1) :
            print(arr[i][j], end = " ")
        print()
 
    


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
n=3
rotateMatrix(matrix,n)
