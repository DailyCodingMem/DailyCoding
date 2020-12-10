import sys
sys.stdin = open("11403in.txt",'r')

from collections import deque
N = int(input())
G = list(list(map(int,input().split())) for _ in range(N))
# G = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
basket = {} # {0: [3], 1: [6], 2: [], 3: [4, 5], 4: [0], 5: [6], 6: [2]}
for i in range(N):
    basket[i] = []
for i in range(N):
    for j in range(N):
        if G[i][j]:
            basket[i].append(j)
answer = list(list(0 for _ in range(N)) for _ in range(N))
for i in range(N):
    myBasket = deque([])
    visited = list(True for _ in range(N))
    for j in basket[i]:
        myBasket.append(j)
        visited[j] = False
    while myBasket:
        point = myBasket.popleft()
        for l in basket[point]:
            if visited[l]:
                visited[l] = False
                myBasket.append(l)

    for k in range(N):
        if not visited[k]:
            answer[i][k] = 1
for i in range(len(answer)):
    print(*answer[i])