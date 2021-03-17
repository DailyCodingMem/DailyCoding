# baekjoon - [16929]TwoDots (2021-01-22)
# https://www.acmicpc.net/problem/16929
import sys
from collections import deque
sys.stdin = open("baekjoon/[16929]TwoDots.txt",'r')

# dfs
def solution(y, x, fin) :
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[False for _ in range(M)] for _ in range(N)]
    st = deque([(y,x,1)])

    while(st) :
        y, x, val = st[-1]
        color = mat[y][x]
        visited[y][x] = True

        if val >= 4 and (y,x) in fin:
            return True

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M :
                if visited[ny][nx] == False and color == mat[ny][nx] :
                    st.append((ny,nx,val+1))
                    break
        else :
            st.pop()
        

    return False

def pos(y,x) :
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    fin = []

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M :
            if mat[y][x] == mat[ny][nx] :
                fin.append((ny,nx))

    return fin
    

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(input()) for _ in range(N)]
    
    result = False

    for i in range(N) :
        for j in range(M) :
            fin = pos(i,j)
            if len(fin) > 1 : 
                result = solution(i, j, fin)
                if result :
                    break
        if result :
            break
    
    if result :
        print('Yes')
    else :
        print('No')