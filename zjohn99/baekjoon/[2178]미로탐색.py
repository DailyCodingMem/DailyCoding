# baekjoon - [2178]미로탐색 (2020-12-08)
# https://www.acmicpc.net/problem/2178
import sys
from collections import deque
sys.stdin = open("baekjoon/[2178]미로탐색.txt",'r')

def solution():
    # 최소 칸 = BFS
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[False for _ in range(M)] for _ in range(N)]
    que = deque([(0,0,1)])
    visited[0][0] = True
    while(que) :
        y, x, cnt = que.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M :
                if visited[ny][nx] == False and mat[ny][nx] == 1 :
                    que.append((ny,nx,cnt+1))
                    visited[ny][nx] = True
                    if (ny+1,nx+1) == (N,M) :
                        return cnt+1

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(map(int, input())) for _ in range(N)]
    print(solution())