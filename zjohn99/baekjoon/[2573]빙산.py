# baekjoon - [2573]빙산 (2020-12-01)
# https://www.acmicpc.net/problem/2573
import sys
from copy import deepcopy
sys.stdin = open("baekjoon/[2573]빙산.txt",'r')

# 시간초과

def solution() :
    years = 0
    cnt_lump = 0
    while(True) :
        melt()
        years += 1
        if len(ice) > 1 :    
            cnt_lump = bfs()
            if cnt_lump == 2 :
                return years    
        else :
            return 0

def melt():
    global mat, ice

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    cp_mat = deepcopy(mat)
    cp_ice = deepcopy(ice)
    
    for i in range(len(ice)) :
        y, x = ice[i]
        for j in range(4) :
            ny = y + dy[j]
            nx = x + dx[j]
            if mat[ny][nx] == 0 :
                cp_mat[y][x] -= 1
                if cp_mat[y][x] == 0 :
                    cp_ice.remove((y,x))   
                    break
    mat = cp_mat
    ice = cp_ice

def bfs():
    global ice
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    st = ice[0]
    cnt = 0

    for ic in range(len(ice)) :
        st = [ice[ic]]
        if visited[st[0][0]][st[0][1]] == 0 :
            cnt += 1
            if cnt == 2 :
                return cnt
            while(st) :
                y, x = st.pop(0)
                visited[y][x] = cnt

                for i in range(4) :
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if mat[ny][nx] != 0 and visited[ny][nx] == 0: 
                        st.append((ny,nx))






    


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    ice = []
    for i in range(1,N-1):
        for j in range(1,M-1) :
            if mat[i][j] != 0 :
                ice.append((i,j))

    print(solution())