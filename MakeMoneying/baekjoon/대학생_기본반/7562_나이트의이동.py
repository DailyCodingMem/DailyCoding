import sys
sys.stdin = open("7562in.txt",'r')

from collections import deque
T = int(input())
for count in range(T):
    I = int(input())
    dy = [-2,-2,-1,-1,1,1,2,2]
    dx = [-1,1,-2,2,-2,2,-1,1]
    visited = list(list(True for _ in range(I)) for _ in range(I))
    startY,startX = map(int,input().split())
    endY,endX = map(int,input().split())
    answer = 0
    basket = deque([(startY,startX,answer)])
    while basket:
        Y,X,answer = basket.popleft()
        if Y == endY and X == endX:
            print(answer)
            break
        
        for i in range(8):
            checkY = Y + dy[i]
            checkX = X + dx[i]
            if 0<= checkY<I and 0 <= checkX<I and visited[checkY][checkX]:
                visited[checkY][checkX] = False
                basket.append((checkY,checkX,answer+1))