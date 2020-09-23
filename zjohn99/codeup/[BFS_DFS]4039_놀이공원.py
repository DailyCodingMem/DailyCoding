# codeup - BFS/DFS - 놀이공원 (2020-09-23)
# https://codeup.kr/problem.php?id=4039
# 최소거리 BFS

import sys
sys.stdin = open("codeup/[BFS_DFS]4039_놀이공원.txt",'r')


## 시간초과 해결
def solution(y,x):
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    st = [(y,x,1)]
    visited[y][x] = True
    while(st) :
        y, x, cnt = st.pop(0)
        block = mat[y][x]

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == False:
                if mat[ny][nx]-1 <= block <= mat[ny][nx]+1:
                    if (ny+1,nx+1) == (n,m) :
                        return cnt+1
                    st.append((ny,nx,cnt+1))
                    visited[ny][nx] = True  # 시간초과 해결 - 이미 들렸던 곳을 또 들리지 않으면 된다.
    else :
        return 0

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    print(solution(0,0))
