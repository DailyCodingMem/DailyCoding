import sys
sys.stdin = open("2667in.txt",'r')

from collections import deque
N = int(input())
List = list(list( int(x) for x in input()) for _ in range(N))
visited = list(list(True for _ in range(N)) for _ in range(N))
dy = [-1,1,0,0]
dx = [0,0,-1,1]
answerBasket = deque([])
checkPoint = 0
for y in range(N):
    for x in range(N):
        if List[y][x] and visited[y][x]:
            checkPoint += 1
            cnt = 1
            visited[y][x] = False
            basket = deque([(y,x)])
            while basket:
                checkY,checkX = basket.popleft()
                for i in range(4):
                    newY = checkY + dy[i]
                    newX = checkX + dx[i]
                    if 0<=newY<N and 0<=newX<N and List[newY][newX] and visited[newY][newX]:
                        visited[newY][newX] = False
                        cnt += 1
                        basket.append((newY,newX))
            answerBasket.append(cnt)
answer = []
for i in answerBasket:
    answer.append(i)
answer.sort()
print(checkPoint)
for i in answer:
    print(i)