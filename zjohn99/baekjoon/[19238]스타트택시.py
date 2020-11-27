# baekjoon - [19238]스타트택시 (2020-10-15)
# https://www.acmicpc.net/problem/19238
from pprint import pprint
import sys
from collections import deque
sys.stdin = open("baekjoon/[19238]스타트택시.txt",'r')

def solution(y, x) :
    global oil
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[False for _ in range(N)] for _ in range(N)]
    print(visited)
    print(y,x)
    st = deque()
    st.append((y,x,0))
    visited[y][x] = True
    # cnt = 0
    while(ctr) :
        y, x, dep = st.popleft()
        
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == False and mat[ny][nx] == 0 :
                    if [ny+1, nx+1] in ctr_st :
                        st.append((ny,nx,dep+1,ctr_st.index([ny+1, nx+1])))
                    else :
                        st.append((ny,nx,dep+1,-1))
                    


    return 0
                






T = int(input())
for t in range(1, T+1):
    N, M, oil = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    sy, sx = map(int, input().split())
    sy, sx = sy-1, sx-1
    ctr = [list(map(int, input().split()))for _ in range(M)] # 손님의 sy,sx ay,ax
    ctr_st = []
    ctr_fin = []
    for i in range(M) :
        ctr_st.append(ctr[i][:2])
        ctr_fin.append(ctr[i][2:4])
 
    solution(sy, sx)