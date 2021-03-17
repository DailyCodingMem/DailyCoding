import sys
sys.stdin = open("13549in.txt",'r')

from collections import deque
N,K = map(int,input().split())
basket = deque([(N,0)])
visited = list(111111 for _ in range(100010))
visited[N] = 0
while basket:
    point,time = basket.popleft()
    cross = point*2
    while cross and cross<=2*K:
        if cross <= 100000 and visited[cross] > time:
            visited[cross]=time
            basket.append((cross,time))
        cross *= 2
    if point+1 <= 100000 and visited[point+1] > time+1:
        visited[point+1] = time+1
        basket.append((point+1,time+1))
    if point-1 >= 0 and visited[point-1] > time+1:
        visited[point-1] = time+1
        basket.append((point-1,time+1))
print(visited[K])