import sys
sys.stdin = open("1260in.txt",'r')

from collections import deque
N,M,V = map(int,input().split())
basket = {}
for i in range(N):
    basket[i+1] = []
for _ in range(M):
    A,B = map(int,input().split())
    basket[A].append(B)
    basket[B].append(A)
for i in range(N):
    basket[i+1].sort()


def DFS(point):
    global DFSAnswer, DFSVisited, DFSBasket

    for j in basket[point]:
        if DFSVisited[j]:
            DFSVisited[j] = False
            DFSAnswer.append(j)
            DFSBasket.append(j)
            DFS(j)

DFSBasket = deque([V])
BFSBasket = deque([V])

DFSAnswer = [V]
BFSAnswer = [V]

DFSVisited = list(True for _ in range(N+1))
BFSVisited = list(True for _ in range(N+1))

DFSVisited[V] = False
BFSVisited[V] = False

DFS(V)

while BFSBasket:
    point = BFSBasket.popleft()
    for j in basket[point]:
        if BFSVisited[j]:
            BFSVisited[j] = False
            BFSAnswer.append(j)
            BFSBasket.append(j)

print(*DFSAnswer)
print(*BFSAnswer)
