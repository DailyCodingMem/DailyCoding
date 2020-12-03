import sys
sys.stdin = open("5014in.txt",'r')

from collections import deque
# 총 F층, 현재 S층, G층에 스타트링크
F,S,G,U,D = map(int,input().split())

basket = deque([(S,0)])
visited = list(True for _ in range(F+1))
visited[S] = False
while basket:
    floor,cnt = basket.popleft()
    if floor==G:
        basket.append(1)
        print(cnt)
        break
    if floor+U <= F and visited[floor+U]:
        visited[floor+U] = False
        basket.append((floor+U,cnt+1))
    if floor-D >= 1 and visited[floor-D]:
        visited[floor-D] = False
        basket.append((floor-D,cnt+1))
if not basket:
    print("use the stairs")