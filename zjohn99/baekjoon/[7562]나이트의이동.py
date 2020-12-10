# baekjoon - [7562]나이트의이동 (2020-12-10)
# https://www.acmicpc.net/problem/7562
import sys
from collections import deque
sys.stdin = open("baekjoon/[7562]나이트의이동.txt",'r')

def solution(sy,sx) :
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    visited = [[False for _ in range(l)] for _ in range(l)]
    
    que = deque([(sy,sx, 0)])
    visited[sy][sx] = True

    while(que) :
        y, x, cnt = que.popleft()
        if (y,x) == (fy,fx) :
            return cnt


        for i in range(8) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < l and 0 <= nx < l :
                if visited[ny][nx] == False :
                    que.append((ny,nx,cnt+1))
                    visited[ny][nx] = True
                    if (ny,nx) == (fy,fx) :
                        return cnt+1

T = int(input())
for t in range(1, T+1):
    l = int(input())
    sy, sx = map(int, input().split())
    fy, fx = map(int, input().split())

    print(solution(sy,sx))