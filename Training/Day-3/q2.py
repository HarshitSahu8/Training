'''
 Write a method Boolean isKingSafe(int[][]chessBoard)
Returns true if king in the given chess board is safe from the given enemies otherwise false;
NOTE: Enemies are- Horse, Camel, Queen, Elephant only
Do not consider the colour case of the chess board for traversal of camel and all.
'''
def horse(King, Horse):
    southLeft=[Horse[0]+2,Horse[1]-1]
    southRight=[Horse[0]+2,Horse[1]+1]
    westLeft=[Horse[0]+1,Horse[1]-2]
    westRight=[Horse[0]-1,Horse[1]-2]
    northLeft=[Horse[0]-2,Horse[1]-1]
    northRight=[Horse[0]-2,Horse[1]+1]
    EastLeft=[Horse[0]-1,Horse[1]+2]
    EastRight=[Horse[0]+1,Horse[1]+2]
    if southLeft[0]==King[0] and southLeft[1]==King[1]:
        return True
    if southRight[0]==King[0] and southRight[1]==King[1]:
        return True
    if westLeft[0]==King[0] and westLeft[1]==King[1]:
        return True
    if westRight[0]==King[0] and westRight[1]==King[1]:
        return True
    if northLeft[0]==King[0] and northLeft[1]==King[1]:
        return True
    if northRight[0]==King[0] and northRight[1]==King[1]:
        return True
    if EastLeft[0]==King[0] and EastLeft[1]==King[1]:
        return True
    if EastRight[0]==King[0] and EastRight[1]==King[1]:
        return True    
    return False
    


def camel(King, Camel,size):
    i=Camel[0]
    j=Camel[1]
    while((i>=0 and j>=0) and(i>size and j>size)):
        if i==King[0] and j==King[1]:
            return True
        i+=1
        j+=1
    i=Camel[0]
    j=Camel[1]
    while(i>=0 and j>=0):
        if i==King[0] and j==King[1]:
            return True
        i-=1
        j+=1
    i=Camel[0]
    j=Camel[1]
    while(i>=0 and j>=0):
        if i==King[0] and j==King[1]:
            return True
        i-=1
        j-=1
    i=Camel[0]
    j=Camel[1]
    while(i>=0 and j>=0):
        if i==King[0] and j==King[1]:
            return True
        i+=1
        j-=1
    return False    


def elephant(King, Elephant):
    if King[0]==Elephant[0] or King[1]==Elephant[1]:
        return True

def queen(King, Queen,size):
    if camel(King,Queen,size):
        return True
    if elephant(King,Queen):
        return True
    return False



def isKingSafe(chess):
    King = [0]*2
    Horse = [0]*2
    Camel = [0]*2
    Queen = [0]*2
    Elephant = [0]*2
    size = len(chess)
    for i in range(size):
        for j in range(size):
            if chess[i][j] == 'K':
                King[0] = i
                King[1] = j
            elif chess[i][j] == 'H':
                Horse[0] = i
                Horse[1] = j
            elif chess[i][j] == 'C':
                Camel[0] = i
                Camel[1] = j
            elif chess[i][j] == 'Q':
                Queen[0] = i
                Queen[1] = j
            elif chess[i][j] == 'E':
                Elephant[0] = i
                Elephant[1] = j

    if horse(King, Horse):
        return False
    if camel(King, Camel,size):
        return False
    if queen(King, Queen,size):
        return False
    if elephant(King, Elephant):
        return False
    return True


board = [['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', 'K', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.']]

print(isKingSafe(board))