import sys
sys.stdin = open("in.txt",'r')

y,x = map(int,input().split())
List = list(list(map(int,input().split())) for _ in range(y))

TF = list(list(False for _ in range(x)) for _ in range(y))

for Y in range(y):
    for X in range(x):
        if List[Y][X]:
            TF[Y][X] = True
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def whiteToBlack(Y,X):
    for i in range(4):
        newY = Y + dy[i]
        newX = X + dx[i]
        if 0<=newY<y and 0<=newX<x and not List[newY][newX]:
            List[newY][newX] = 1
            whiteToBlack(newY,newX)

def blackToWhite(Y,X):
    for i in range(4):
        newY = Y + dy[i]
        newX = X + dx[i]
        if 0<=newY<y and 0<=newX<x and TF[newY][newX]:
            TF[newY][newX] = False
            blackToWhite(newY,newX)

black = white = 0
for Y in range(y):
    for X in range(x):
        if not List[Y][X]:
            List[Y][X] = 1
            white += 1
            whiteToBlack(Y,X)
        if TF[Y][X]:
            black += 1
            TF[Y][X] = False
            blackToWhite(Y,X)

print(white,black)
