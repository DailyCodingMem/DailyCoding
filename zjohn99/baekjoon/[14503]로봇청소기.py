# baekjoon - [14503]로봇청소기 (2020-11-27)
# https://www.acmicpc.net/problem/14503
import sys
sys.stdin = open("baekjoon/[14503]로봇청소기.txt",'r')

def solution(r,c,d):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[False for _ in range(M)] for _ in range(N)]
    st = [(r,c,d)]
    sweep = 1
    visited[r][c] = True

    while(st) :
        y, x, d = st.pop()

        # 2-1,2 조건
        for i in range(1,5) :
            tmp_d = d - i
            if tmp_d < 0 :
                tmp_d = 4 + d - i

            ny = y + dy[tmp_d]
            nx = x + dx[tmp_d]

            if(0 <= ny < N and 0 <= nx < M) :
                if(mat[ny][nx] == 0 and visited[ny][nx] == False) :
                    visited[ny][nx] = True
                    st.append((ny,nx,tmp_d))
                    sweep += 1
                    break
        else :
            ny = y - dy[d]
            nx = x - dx[d]
            # 2-3,4 조건
            if(mat[ny][nx] == 1) :
                return sweep
            else :
                st.append((ny,nx,d))

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]

    print(solution(r,c,d))
    