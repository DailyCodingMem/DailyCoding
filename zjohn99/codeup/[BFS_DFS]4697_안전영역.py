# codeup - BFS/DFS - 안전영역 (2020-09-30)
# https://codeup.kr/problem.php?id=4697

import sys
from pprint import pprint
sys.stdin = open("codeup/[BFS_DFS]4697_안전영역.txt",'r')

def solution(h):
    


    return section.append(cnt)

T = int(input())
for _ in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    high = []

    for i in range(N) :
        for j in range(N) :
            if mat[i][j]-1 not in high :
                high.append(mat[i][j]-1)
    high.sort()

    for h in high :
        sink = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N) :
            for j in range(N) :
                if mat[i][j] <= h :
                    sink[i][j] = True
        for i in range()
        solution()
