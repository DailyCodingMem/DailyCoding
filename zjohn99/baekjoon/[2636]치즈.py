# baekjoon - [2636]치즈 (2021-01-25)
# https://www.acmicpc.net/problem/2636

import sys
from collections import deque
from copy import deepcopy
from pprint import pprint
sys.stdin = open("baekjoon/[2636]치즈.txt",'r')

def solution(mat) :
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    cp_mat = deepcopy(mat)
    visited = [[False for _ in range(M)] for _ in range(N)]

    que = deque([(0,0)])

    while(que) :
        y, x = que.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M :
                if mat[ny][nx] == 0 and visited[ny][nx] == False :
                    que.append((ny,nx))
                    visited[ny][nx] = True

                if mat[ny][nx] == 1 :
                    cp_mat[ny][nx] = 0
    return cp_mat

def countCheese() :
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if mat[i][j] == 1 :
                cnt += 1

    return cnt 

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # 세로, 가로
    mat = [list(map(int, input().split())) for _ in range(N)]
    tmp = countCheese()
    result = [tmp]
    while(tmp != 0) :
        mat = solution(mat) 
        tmp = countCheese()
        result.append(tmp)

    print(len(result)-1)
    print(result[-2])
