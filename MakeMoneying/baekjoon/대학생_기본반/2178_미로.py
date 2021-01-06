import sys
sys.stdin = open("2178in.txt",'r')

from collections import deque
N,M = map(int,input().split())
maze = list(list(int(x) for x in input()) for _ in range(N))
basket = deque([(0,0,1)])

dy = [-1,1,0,0]
dx = [0,0,-1,1]
visited = list(list(True for _ in range(M)) for _ in range(N))
visited[0][0] = False
while basket:
    newY, newX, cnt = basket.popleft()
    if newY == N-1 and newX == M-1:
        print(cnt)
        break
    for i in range(4):
        checkY = newY + dy[i]
        checkX = newX + dx[i]
        if 0<= checkY < N and 0 <= checkX < M and visited[checkY][checkX] and maze[checkY][checkX]:
            visited[checkY][checkX] = False
            basket.append((checkY,checkX,cnt+1))
