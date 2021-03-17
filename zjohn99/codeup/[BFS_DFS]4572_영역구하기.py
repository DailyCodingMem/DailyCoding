# codeup - BFS/DFS - 영역구하기 (2020-09-29)
# https://codeup.kr/problem.php?id=4572

import sys
from pprint import pprint
sys.stdin = open("codeup/[BFS_DFS]4572_영역구하기.txt",'r')

def solution(y, x):
    global section
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    st = [(y,x)]
    cnt = 1
    while(st) :
        y, x = st[-1]
        mat[y][x] = True
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < M and 0 <= nx < N :
                if mat[ny][nx] == False :
                    st.append((ny,nx))
                    cnt += 1
                    break
        else :
            st.pop()

    return section.append(cnt)

T = int(input())
for _ in range(T):
    
    M, N, K = map(int, input().split())
    rec = [list(map(int, input().split())) for _ in range(K)]
    mat = [[False for _ in range(N)] for _ in range(M)]
    section = []

    for r in rec :
        ax, ay, bx, by = r
        for y in range(ay, by):
            for x in range(ax, bx) :
                mat[y][x] = True

    # pprint(mat)
    for y in range(0, M) :
        for x in range(0, N) :
            if mat[y][x] == False :
                solution(y, x)

    section.sort()
    print(len(section))
    for i in section :
        print(i, end=" ")
