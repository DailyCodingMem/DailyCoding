dy = [-1,1,0,0]
dx = [0,0,-1,1]

def miro(y,x):
    List[y][x] = "*"
    for i in range(4):
        Y = y+dy[i]
        X = x+dx[i]
        if 0<=Y<10 and 0<=X<10 and List[Y][X] == "_":
            List[Y][X] = "*"
            miro(Y,X)


List = [list(x for x in input()) for _ in range(10)]
X,Y = map(int,input().split())

if List[Y][X] == "_":
    miro(Y,X)

for i in range(10):
    print("".join(List[i]))
# __________
# _____****_
# _____*__*_
# __*******_
# __*__*_**_
# __*__****_
# __*____*__
# __*____*__
# __******__
# __________
# 6 2