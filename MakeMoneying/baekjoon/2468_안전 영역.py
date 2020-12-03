import sys
sys.stdin = open("2468in.txt",'r')

from collections import deque

N = int(input())
List = []
Max = 0
for _ in range(N):
    line = list(map(int,input().split()))
    List.append(line)
    lineMax = max(line)
    if Max < lineMax:
        Max = lineMax
# print(List,Max)
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def rainCheck(y,x):
    global visited
    visited[y][x] = False
    basket = deque([(y,x)])
    while basket:
        checkY,checkX = basket.popleft()
        for i in range(4):
            newY = checkY + dy[i]
            newX = checkX + dx[i]
            if 0<= newY < N and 0<= newX<N and List[newY][newX] and visited[newY][newX]:
                visited[newY][newX] = False
                basket.append((newY,newX))
                
rain = 1
answer = [1]
while rain <= Max:
    for y in range(N):
        for x in range(N):
            if List[y][x] and List[y][x] <= rain:
                List[y][x] = 0

    visited = list(list(True for _ in range(N)) for _ in range(N))
    cnt = 0
    for y in range(N):
        for x in range(N):
            if List[y][x] and visited[y][x]:
                cnt += 1
                rainCheck(y,x)
    answer.append(cnt)
    rain += 1
print(max(answer))