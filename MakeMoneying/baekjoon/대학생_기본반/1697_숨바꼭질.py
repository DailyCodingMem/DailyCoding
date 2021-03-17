import sys
sys.stdin = open("1697in.txt",'r')

from collections import deque
N,K = map(int,input().split())
basket = deque([(N,0)])
checkPoint = list(True for _ in range(1000000))
while True:
    point,cnt = basket.popleft()
    if point == K:
        print(cnt)
        break
    else:
        A,B,C = point-1,point+1,point*2
        if 0<=A and checkPoint[A]:
            checkPoint[A] = False
            basket.append((A,cnt+1))
        if B<=1e5 and checkPoint[B]:
            checkPoint[B] = False
            basket.append((B,cnt+1))
        if C<=1e5 and checkPoint[C]:
            checkPoint[C] = False
            basket.append((C,cnt+1))