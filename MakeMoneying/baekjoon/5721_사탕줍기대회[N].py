import sys
sys.stdin = open("5721in.txt",'r')

def mossol(y,x):
    # 윗줄
    checkY = y-1
    if 0<=checkY:
        for i in range(M):
            candy[checkY][i]=0
    # 아랫줄
    checkY = y+1
    if checkY<M:
        for i in range(M):
            candy[checkY][i] = 0
    #왼 오
    leftX = x-1
    rightX = x+1
    if 0<=leftX:
        candy[y][leftX]=0
    if rightX<N:
        candy[y][rightX]=0
    return candy
def mosol(y,x):
    # 윗줄
    checkY = y-1
    if 0<=checkY:
        for i in range(M):
            currentCandy[checkY][i][0]=0
    # 아랫줄
    checkY = y+1
    if checkY<M:
        for i in range(M):
            currentCandy[checkY][i][0]=0
    #왼 오
    leftX = x-1
    rightX = x+1
    if 0<=leftX:
        currentCandy[y][leftX][0]=0
    if rightX<N:
        currentCandy[y][rightX][0]=0
def bubsa(y,x):
    # 윗줄
    checkY = y-1
    if 0<=checkY:
        for i in range(M):
            currentCandy[checkY][i][0]=currentCandy[checkY][i][1]
    # 아랫줄
    checkY = y+1
    if checkY<M:
        for i in range(M):
            currentCandy[checkY][i][0]=currentCandy[checkY][i][1]
    #왼 오
    leftX = x-1
    rightX = x+1
    if 0<=leftX:
        currentCandy[y][leftX][0]=currentCandy[y][leftX][1]
    if rightX<N:
        currentCandy[y][rightX][0]=currentCandy[y][rightX][1]

    
def cech(result,candy):
    global M,N,Max

    if result > Max:
        Max = result

    for Y in range(M):
        for X in range(N):
            if visited[Y][X] and candy[Y][X]:
                visited[Y][X] = 0
                # mosol(Y,X)
                cech(result+candy[Y][X],mossol(Y,X))
                # bubsa(Y,X)
                visited[Y][X] = 1


while True:
    M,N = map(int,input().split())
    if M==N and not M:
        break
    candy = list(list(map(int,input().split())) for _ in range(M))
    currentCandy = list(list() for _ in range(M))
    for y in range(M):
        for x in range(N):
            currentCandy[y].append([candy[y][x],candy[y][x]])
    visited = list(list(1 for _ in range(N))for _ in range(M))
    result = 0
    Max = 0
    cech(0,candy)
    print(Max)