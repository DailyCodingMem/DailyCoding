# 0 0 0 0 0 0 0 0 1 
# 0 0 0 0 0 0 0 0 0 
# 0 0 0 1 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 1 0 0 0 
# 0 0 0 0 0 1 0 0 1 
# 0 0 1 0 1 1 0 0 0 
# 0 0 0 0 1 0 0 1 0 
# 0 0 0 0 0 0 0 0 0 
# 2 2

List = [list(map(int,input().split())) for _ in range(9)]
A,B = map(int,input().split())
dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]
Mine = [list( '_' for x in range(9)) for _ in range(9)]
A-=1
B-=1
def Mining(y,x):
    
    mines = 0
    for i in range(8):
        Y = y+dy[i]
        X = x+dx[i]
        if 0<=Y<9 and 0<=X<9 and List[Y][X]:
            mines += 1
    Mine[y][x] = mines
    if not mines:
        for i in range(8):
            Y = y+dy[i]
            X = x+dx[i]
            if 0<=Y<9 and 0<=X<9 and Mine[Y][X]=='_':
                Mining(Y,X)
if List[A][B]:
    Mine[A][B] = -1
else:
    Mining(A,B)
for i in range(9):
    for j in range(9):
        print(Mine[i][j],end=" ")
    print()
