# swea - [1953]탈주범 검거 (2021-01-19)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq&categoryId=AV5PpLlKAQ4DFAUq&categoryType=CODE

import sys
from collections import deque
sys.stdin = open("swea/[1953]탈주범검거.txt",'r')

def solution(y, x, L) :
    dy = [-1, 0, 1, 0] # 상 우 하 좌
    dx = [0, 1, 0, -1]

    d_type = {
        1 : [0, 1, 2, 3], # 상하좌우
        2 : [0, 2], # 상하
        3 : [1, 3], # 좌우
        4 : [0, 1], # 상우
        5 : [1, 2], # 우하
        6 : [2, 3], # 하좌
        7 : [0, 3]  # 상좌
    }

    d_pos = {
        0 : [1, 2, 5, 6], # 0번이왔을때, 이어지는 파이프번호
        1 : [1, 3, 6, 7],
        2 : [1, 2, 4, 7],
        3 : [1, 3, 4, 5]
    }

    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[y][x] = True
    sec = 1
    que = deque([(y, x, sec)])
    cnt = 1

    while(que) :        
        y, x, sec = que.popleft()
        
        if sec == L :
            return cnt
            
        pipe = mat[y][x]

        for p in d_type[pipe] :
            ny = y + dy[p]
            nx = x + dx[p]


            if 0 <= ny < N and 0 <= nx < M :
                if mat[ny][nx] in d_pos[p] and visited[ny][nx] == False :
                    que.append((ny,nx,sec+1))
                    visited[ny][nx] = True
                    cnt += 1
            
    return cnt
        
T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    print('#{0} {1}'.format(t, solution(R, C, L)))
