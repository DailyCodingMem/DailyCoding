import sys
sys.stdin = open("7569in.txt",'r')

from collections import deque
dz = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dx = [0,0,0,0,-1,1]
def inspection():
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if not tomato[z][y][x]:
                    return False
    return True
def ripeTomato():
    global checkPoint, maxDay
    maxDay = 0
    visited = list(list(list(True for _ in range(M)) for _ in range(N))for _ in range(H))
    while basket:
        Z,Y,X,day = basket.popleft()
        for i in range(6):
            newZ = Z + dz[i]
            newY = Y + dy[i]
            newX = X + dx[i]
            if 0<=newZ<H and 0<=newY<N and 0<=newX<M and visited[newZ][newY][newX] and not tomato[newZ][newY][newX]:
                visited[newZ][newY][newX] = False
                tomato[newZ][newY][newX] = 1
                basket.append((newZ,newY,newX,day+1))
                maxDay = max(day+1,maxDay)
                if checkPoint:
                    checkPoint = False
M,N,H = map(int,input().split())
tomato = list(list(list(map(int,input().split())) for _ in range(N)) for _ in range(H))

day = maxDay = 0
checkPoint = True
basket = deque([])
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[z][y][x]==1:
                basket.append((z,y,x,day))
ripeTomato()
if inspection():
    print(maxDay)
else:
    print(-1)