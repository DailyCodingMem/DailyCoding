import sys
sys.stdin = open("2606in.txt",'r')

from collections import deque
com = int(input())
count = int(input())
basket = {}
for i in range(com+1):
    basket[i] = []
for _ in range(count):
    A,B = map(int,input().split())
    basket[A].append(B)
    basket[B].append(A)

visited = [ True for _ in range(com+1) ]
visited[1] = False
virus = deque([1])
answer = 0
while virus:
    computer = virus.popleft()
    for i in basket[computer]:
        if visited[i]:
            visited[i] = False
            answer += 1
            virus.append(i)
print(answer)
