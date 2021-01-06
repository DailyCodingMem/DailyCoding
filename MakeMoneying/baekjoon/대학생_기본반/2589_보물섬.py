import sys
sys.stdin = open("2589in.txt",'r')

from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def wheretogo(a,b):
    global answer
    basket = deque([(a,b,0)])
    visited = list(list(True for _ in range(X)) for _ in range(Y))
    visited[a][b] = False
    while basket:
        newY,newX,distance = basket.popleft()
        if answer < distance:
            answer = distance
        for i in range(4):
            checkY = newY + dy[i]
            checkX = newX + dx[i]
            if 0<= checkY < Y and 0 <= checkX < X and treasure[checkY][checkX] == "L" and visited[checkY][checkX]:
                visited[checkY][checkX] = False
                basket.append((checkY,checkX,distance+1))

Y,X = map(int,input().split())
treasure = list(list(x for x in input()) for _ in range(Y))
answer = 0
for y in range(Y):
    for x in range(X):
        if treasure[y][x] == "L":
            wheretogo(y,x)
print(answer)