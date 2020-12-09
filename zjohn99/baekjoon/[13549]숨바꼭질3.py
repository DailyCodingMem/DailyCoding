# baekjoon - [13549]숨바꼭질3 (2020-12-09)
# https://www.acmicpc.net/problem/13549

# 꼭 다시한번더 풀어보기!!!!!!!!!!!!
import sys
from collections import deque
sys.stdin = open("baekjoon/[13549]숨바꼭질3.txt",'r')

def solution() :
    dx = [1, -1, 2]
    visited = [9999999 for _ in range(100001)]
    que = deque([(N)])
    visited[N] = 0
    
    # 같았을때 생각해주기
    if N == K :
        return visited[N]

    while(que) :
        x = que.popleft()
        if x == K :
            return visited[x]

        for i in range(3) :
            if i == 2 :
                nx = x * dx[i]
            else :
                nx = x + dx[i]

            if 0 <= nx <= 100000:
                t = visited[x]
                tmp_time = visited[nx]
                if i == 2 :
                    if tmp_time > t :
                        que.append((nx))
                        visited[nx] = t
                        
                else :
                    if tmp_time > t+1 :
                        que.append((nx))
                        visited[nx] = t+1
                        
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())

    print(solution())