import sys
sys.stdin = open("11724in.txt",'r')

from collections import deque
N,M = map(int,input().split())
upBasket = {}
downBasket = {}
for i in range(N):
    upBasket[i+1] = []
    downBasket[i+1] = []
for _ in range(M):
    A,B = map(int,input().split())
    upBasket[A].append(B)
    downBasket[B].append(A)
visited = list(True for _ in range(N+1))
answer = 0
for i in range(N):
    if visited[i+1]:
        answer += 1
        visited[i+1] = False
        checkBasket = deque([i+1])
        while checkBasket:
            point = checkBasket.popleft()
            for up in upBasket[point]:
                if visited[up]:
                    visited[up] = False
                    checkBasket.append(up)
            for down in downBasket[point]:
                if visited[down]:
                    visited[down] = False
                    checkBasket.append(down)
print(answer)