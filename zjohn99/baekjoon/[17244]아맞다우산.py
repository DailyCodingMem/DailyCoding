# baekjoon - [17244]아맞다우산 (2021-01-20)
# https://www.acmicpc.net/problem/17244
import sys
from collections import deque
from pprint import pprint
from copy import deepcopy
sys.stdin = open("baekjoon/[17244]아맞다우산.txt",'r')

# def solution(item) :
#     dy = [-1, 0, 1, 0]
#     dx = [0, 1, 0, -1]
#     cnt = 0

#     for i in range(len(item)-1) :
#         s = item[i]
#         e = item[i+1]
#         visited = [[False for _ in range(N)] for _ in range(M)]
#         y, x = s
#         val = 0
#         visited[y][x] = True
#         que = deque([(y,x,val)])
#         check = True
#         while(check) :
#             y, x, val = que.popleft()

#             for j in range(4) : 
#                 ny = y + dy[j]
#                 nx = x + dx[j]

#                 if 0 <= ny < M and 0 <= nx < N :
#                     if mat[ny][nx] != '#' and visited[ny][nx] == False :
#                         que.append((ny, nx, val+1))
#                         visited[ny][nx] = True

#                 if e == (ny,nx) :
#                     check = False
#                     cnt += val+1
#                     break
#     return cnt

# def perm(arr, s, e) :
#     global len_items

#     if s == e :
#         tmp = deepcopy(arr) # 이부분을 어떻게 해야할까 그냥 append를 하면 같은 주소라서 바뀌어버림
#         all_items.append(tmp)
#         len_items += 1
#         return
    
#     for idx in range(s, e) :
#         arr[idx], arr[s] = arr[s], arr[idx]
#         perm(arr, s+1, e)
#         arr[idx], arr[s] = arr[s], arr[idx]


# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     mat = [list(input()) for _ in range(M)]
#     start = []
#     end = []
#     items = []

#     for i in range(M) :
#         for j in range(N) :
#             if mat[i][j] == 'S' :
#                 start.append((i,j))
#             elif mat[i][j] == 'X' :
#                 items.append((i,j))
#             elif mat[i][j] == 'E' :
#                 end.append((i,j))
#     items = start + items + end 
#     all_items = []
#     len_items = 0
#     perm(items, 1, len(items)-1)

#     results = [0 for _ in range(len_items)]

#     for i in range(len_items) :
#         results[i] = solution(all_items[i])

#     print(min(results))

T = int(input())
for t in range(1, T+1):
    dir = [[1,0],[0,1],[-1,0],[0,-1]]
    m,n = map(int, input().split())
    tmp = [input() for i in range(n)]
    arr = [[0]*m for i in range(n)]
    k = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 'S':
                si,sj = i,j
            elif tmp[i][j] == 'E':
                ei,ej = i,j
            elif tmp[i][j] == '#':
                arr[i][j] = -1
            elif tmp[i][j] == 'X':
                arr[i][j] = k = k + 1
    
    pprint(arr)
    visited = [[[0]*(2**k) for j in range(m)] for i in range(n)]

    pprint(visited)
    que = deque([[si,sj,0]])
    res,cnt = -1, 0
    ef = (2**k)-1
    print(bin(ef))

    while que and res == -1:
        for _ in range(len(que)):
            i,j,f = que.popleft()

            if i == ei and j == ej and f == ef: 
                res = cnt

            for d in range(4):
                ni,nj,nf = i + dir[d][0], j + dir[d][1],f
                if 0 <= ni < n and 0 <= nj < m and arr[i][j] != -1:
                    if arr[i][j]:
                        nf |= 1<<(arr[i][j]-1)
                        # a |= b --> a와 b의 비트를 or 연산후 결과를 a에 할당
                    if visited[ni][nj][nf]: continue
                    visited[ni][nj][nf] = 1
                    que.append([ni,nj,nf])
        cnt += 1
    print(res)