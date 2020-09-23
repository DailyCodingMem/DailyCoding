# codeup - BFS/DFS - 호수의수구하기 (2020-09-22)
# https://codeup.kr/problem.php?id=4024


import sys
sys.stdin = open("codeup/[BFS_DFS]4024_호수의수구하기.txt",'r')

def solution(y, x):
    dy = [-1,-1,0,1,1,1,0,-1]
    dx = [0,1,1,1,0,-1,-1,-1]
    st = [(y,x)]
    visited[y][x] = True

    while(st) :
        y, x = st[-1]
        for i in range(8) :
            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= 0 and ny < h and nx >=0 and nx < w :
                if visited[ny][nx] == False and mat[ny][nx] == 'L':
                    st.append((ny,nx))
                    visited[ny][nx] = True
                    break
        else :
            st.pop(-1)

    return 1
 
T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    mat = [list(map(str,input().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    val = 0
    for i in range(h) :
        for j in range(w) :
            if mat[i][j] == 'L' and visited[i][j] == False: 
                val += solution(i, j)

    print(val)


