# codeup - BFS/DFS - 위상정렬 (2020-09-17)
# https://codeup.kr/problem.php?id=3212
# LG cns 문제랑 비슷

import sys
sys.stdin = open("codeup/[BFS_DFS]3212_위상정렬.txt",'r')

def solution():
    st = [1]
    visited[1] = True

    while(st) :

        pass


    return 0


T = int(input())
for _ in range(T):
    v, n = map(int, input().split())
    graph = {}
    visited = [False for _ in range(v+1)]
    for i in range(n):
        a, b = map(int, input().split())
        if a not in graph :
            graph[a] = [b]
        else :
            graph[a] += [b]

    solution()