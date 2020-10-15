# baekjoon - [15683]감시 (2020-10-15)
# https://www.acmicpc.net/problem/15683

import sys
sys.stdin = open("baekjoon/[15683]감시.txt",'r')

def solution(y, x, num) :
    global blind
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    cctv = {
        1 : [[0], [1], [2], [3]],
        2 : [[0,2], [1,3]],
        3 : [[0,1], [1,2], [2,3], [3,0]],
        4 : [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
        5 : [[0,1,2,3]]
    }
    cam = [[] for _ in range(len(cctv[num]))]
    view = [[] for _ in range(len(cctv[num]))]
    max_val = 0

    for i in range(len(cctv[num])):
        cnt = 0
        for j in cctv[num][i] : # 수정
            p = 1
            while(True) :
                ny = y + dy[j] * p
                nx = x + dx[j] * p
                p += 1

                # print((ny,nx))
                if 0 <= ny < N and 0 <= nx < M :
                    if mat[ny][nx] == 6 :
                        break
                    elif mat[ny][nx] == 0 :
                        cam[i].append((ny,nx))
                        cnt += 1
                else :
                    break


        view[i].append(cnt)
    
    max_val = view.index(max(view))
    for c in cam[max_val] :
        ny, nx = c
        mat[ny][nx] = -1
   
    blind -= max(view)[0]



T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    blind = 0
    

    for i in range(N):
        for j in range(M):
            if mat[i][j] == 0 :
                blind += 1

    for i in range(N):
        for j in range(M) :
            if mat[i][j] == 6 :
                visited[i][j] = True
            elif 1 <= mat[i][j] <= 5 :
                visited[i][j] = True
                solution(i, j, mat[i][j]) # cctv 위치


    print(blind)

