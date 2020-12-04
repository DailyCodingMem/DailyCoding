import sys
sys.stdin = open("2644in.txt",'r')

from collections import deque
people = int(input())
start, end = map(int,input().split())
count = int(input())
children = {}
parents = {}
visited = [True for _ in range(people+2)]
for i in range(people+1):
    children[i] = []
    parents[i] = []

def isYourChild(A,B):
    basket = deque([(A,0)])
    while basket:
        point,cnt = basket.popleft()
        visited[point] = False
        if point == end:
            return cnt
        # 자식들 담기
        for child in children[point]:
            if visited[child]:
                basket.append((child,cnt+1))
                visited[child] = False
        # 부모 담기
        for parent in parents[point]:
            if visited[parent]:
                basket.append((parent,cnt+1))
                visited[parent] = False
    return -1

for _ in range(count):
    A, B = map(int,input().split())
    children[A].append(B)
    parents[B].append(A)
print(isYourChild(start,end))