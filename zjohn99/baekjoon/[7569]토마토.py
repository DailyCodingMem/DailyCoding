# baekjoon - [7569]토마토 (2020-12-03)
# https://www.acmicpc.net/problem/7569

import sys
from collections import deque
sys.stdin = open("baekjoon/[7569]토마토.txt",'r')

def solution():
    dy = [-1, 0, 1, 0, 0, 0]
    dx = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    answer = 0
    dq = deque()
    dq.extend(ripe)
    while(dq) :
        z,y,x = dq.popleft()
        
        for i in range(6) :
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M :
                if box[nz][ny][nx] == 0 and check[nz][ny][nx] == 0:
                    box[nz][ny][nx] = 1
                    check[nz][ny][nx] = check[z][y][x] + 1
                    answer = check[nz][ny][nx]
                    dq.append((nz,ny,nx))
                    # not_ripe.remove((nz,ny,nx))

    # print(not_ripe)
    # if len(not_ripe) > 0 :
    #     return -1
    # else :
    #     return answer
    for i in range(H) :
        for j in range(N) :
            for k in range(M) :
                if box[i][j][k] == 0 :
                    return -1   
    return answer

T = int(input())
for t in range(1, T+1):
    M, N, H = map(int, input().split())
    box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    check = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
    
    ripe = []
    not_ripe = []

    for h in range(H) :
        for n in range(N) :
            for m in range(M):
                if box[h][n][m] == 1 :
                    ripe.append((h,n,m))
                elif box[h][n][m] == 0 :
                    not_ripe.append((h,n,m))

    print(solution())