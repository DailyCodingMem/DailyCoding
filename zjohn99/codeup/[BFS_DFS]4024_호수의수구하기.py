# codeup - BFS/DFS - 호수의수구하기 (2020-09-22)
# https://codeup.kr/problem.php?id=4024


import sys
sys.stdin = open("codeup/[BFS_DFS]4024_호수의수구하기.txt",'r')



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