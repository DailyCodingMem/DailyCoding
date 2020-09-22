# codeup - BFS/DFS - 오목 (2020-09-21)
# https://codeup.kr/problem.php?id=4023


import sys
sys.stdin = open("codeup/[BFS_DFS]4023_오목.txt",'r')















T = int(input())
for _ in range(T):
    mat = [list(map(int, input().split())) for _ in range(19)]
    visited = [[False for _ in range(19)] for _ in range(19)]
    
    for i in range(19):
        for j in range(19):
            if mat[i][j] != 0 and visited[i][j] == False:
                y,x = i,j
                color = mat[i][j]
                cnt = 1
                visited[y][x] = True
                solution(y,x,-1)














# def solution(y,x,dir):
#     global cnt
#     global st
#     dy = [-1,-1,0,1,1,1,0,-1]
#     dx = [0,1,1,1,0,-1,-1,-1]
#     color = mat[y][x]
#     y, x = st[-1]
#     if dir == -1 :
#         for i in range(8):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if ny >= 0 and ny < 19 and nx >= 0 and nx < 19 :
#                 if mat[ny][nx] == color and visited[ny][nx] == False:
#                     st.append((ny,nx))
#                     # check[ny][nx] = True
#                     cnt += 1
#                     solution(ny,nx,i)
                    
#     else :
#         ny = y + dy[dir]
#         nx = x + dx[dir]
#         if ny >= 0 and ny < 19 and nx >= 0 and nx < 19 :
#             if mat[ny][nx] == color and visited[ny][nx] == False:
#                 st.append((ny,nx))
#                 # check[ny][nx] = True
#                 cnt += 1
#                 if cnt == 5 :
#                     print(color)
#                     ans_y, ans_x = st[0]
#                     print(ans_y+1, ans_x+1)
#                     return
#                 solution(ny,nx,dir)
#             else :
#                 dir = -1
#                 cnt -= 1
#                 st.pop()
#                 return

            
#         else :
#             dir = -1
#             cnt -= 1
#             st.pop()
#             return
#     return 0

# T = int(input())
# for _ in range(T):
#     mat = [list(map(int, input().split())) for _ in range(19)]
#     visited = [[False for _ in range(19)] for _ in range(19)]
    
#     for i in range(19):
#         for j in range(19):
#             if mat[i][j] != 0 and visited[i][j] == False:
#                 y,x = i,j
#                 color = mat[i][j]
#                 st = [(y,x)]
#                 cnt = 1
#                 visited[y][x] = True
#                 solution(y,x,-1)