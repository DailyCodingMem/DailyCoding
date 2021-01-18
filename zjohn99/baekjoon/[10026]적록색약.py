# baekjoon - [10026]적록색약 (2021-01-15)
# https://www.acmicpc.net/problem/10026
import sys
from collections import deque
sys.stdin = open("baekjoon/[10026]적록색약.txt",'r')

def solution(eye, y, x, cnt) :
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    que = deque([(y,x)])
    color = mat[y][x]
    visited[y][x] = cnt

    while(que) :
        y, x = que.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N :
                if eye == 0 : # 색약 x 
                    if color == mat[ny][nx] and visited[ny][nx] == 0:
                        que.append((ny,nx))
                        visited[ny][nx] = cnt
                else : # 색약 o 
                    if (color == mat[ny][nx] or (color == "R" and mat[ny][nx] == "G") or (color == "G" and mat[ny][nx] == "R"))  and visited[ny][nx] == 0 :
                        que.append((ny,nx))
                        visited[ny][nx] = cnt


T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [list(map(str, input())) for _ in range(N)]

    for eye in range(2) :
        visited = [[0 for _ in range(N)] for _ in range(N)]
        cnt = 0
        for i in range(N) :
            for j in range(N) :
                if visited[i][j] == 0 :
                    cnt += 1
                    solution(eye, i, j, cnt)
                    

        print(cnt, end=" ")