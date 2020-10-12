# swea - [1953]탈주범 검거 (2020-10-12)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq&categoryId=AV5PpLlKAQ4DFAUq&categoryType=CODE

import sys
sys.stdin = open("swea/[1953]탈주범검거.txt",'r')

def solution():
    dy = [-1, 0, 1, 0] # 상 우 하 좌
    dx = [0, 1, 0, -1]

    d_type = {
        1 : [0, 1, 2, 3], # 상하좌우
        2 : [0, 2], # 상하
        3 : [1, 3], # 좌우
        4 : [0, 1], # 상우
        5 : [1, 2], # 우하
        6 : [2, 3], # 하좌
        7 : [0, 3]  # 상좌
    }

    d_pos = {
        0 : [1, 2, 5, 6], # 0번이왔을때, 이어지는 파이프번호
        1 : [1, 3, 6, 7],
        2 : [1, 2, 4, 7],
        3 : [1, 3, 4, 5]
    }
    
    st = [(R, C)]
    hour = 1
    cnt = 1
    visited[R][C] = hour
    while(st) :
        y, x = st.pop(0)
        
        if visited[y][x] >= L :
            break

        info = mat[y][x] # d_type의 수

        for d in d_type[info] :
            ny = dy[d] + y
            nx = dx[d] + x

            if 0 <= ny < N and 0 <= nx < M :
                if visited[ny][nx] == 0 and mat[ny][nx] in d_pos[d] : # 방문한 곳과 막혔는지를 체크하는 부분
                    
                    st.append((ny, nx))
                    visited[ny][nx] = visited[y][x] + 1
                    cnt += 1
    return cnt


T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    # 세로 N, 가로 M
    # 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    print('#{0} {1}'.format(t, solution()))
    
