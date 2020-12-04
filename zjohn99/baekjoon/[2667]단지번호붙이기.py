# baekjoon - [2667]단지번호붙이기 (2020-12-04)
# https://www.acmicpc.net/problem/2644
import sys
from collections import deque
sys.stdin = open("baekjoon/[2667]단지번호붙이기.txt",'r')

def solution(i, j, val) :
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    st = deque([(i,j)])
    cnt = 1
    visited[i][j] = val

    while(st) :
        y, x = st.popleft()
        
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N :
                if mat[ny][nx] == 1 and visited[ny][nx] == 0 :
                    visited[ny][nx] = val
                    st.append((ny,nx))
                    cnt += 1

    return cnt

T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    val = 1
    ls_val = []
    for i in range(N) :
        for j in range(N) :
            if mat[i][j] == 1 and visited[i][j] == 0 :
                ls_val.append(solution(i, j, val))
                val += 1
    print('--------------------')
    print(len(ls_val))
    ls_val.sort()
    for i in range(len(ls_val)):
        print(ls_val[i])


