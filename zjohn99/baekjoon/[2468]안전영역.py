# baekjoon - [2468]안전영역 (2020-12-02)
# https://www.acmicpc.net/problem/2468
import sys
sys.stdin = open("baekjoon/[2468]안전영역.txt",'r')

def solution():
    safe = [1]
    len_hq = len(hq)
    for _ in range(len_hq) :
        ls = sink()
        if len(ls) > 0 :
            safe.append(bfs(ls))  
    return max(safe)


def sink() :
    st = []
    rain = hq.pop(0)
    for i in range(N) :
        for j in range(N) :
            if mat[i][j] <= rain :
                mat[i][j] = 0
            if mat[i][j] != 0 :
                st.append((i,j))
    return st


def bfs(ls) :
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    st = []
    for l in ls :
        ty, tx = l
        if visited[ty][tx] == 0 :
            cnt += 1
            st.append(l)
            visited[ty][tx] = cnt
            while(st) :
                y,x = st.pop(0)
                
                for i in range(4) :
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if 0 <= ny < N and 0 <= nx < N :
                        if visited[ny][nx] == 0 and mat[ny][nx] != 0:
                            visited[ny][nx] = cnt
                            st.append((ny,nx))
    return cnt

T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    hq = []
    for i in range(N):
        for j in range(N):
            if mat[i][j] not in hq :
                hq.append(mat[i][j])
    hq.sort()
    print(solution())    
