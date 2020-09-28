# codeup - BFS/DFS - 바이러스 (2020-09-28)
# https://codeup.kr/problem.php?id=4503

import sys
sys.stdin = open("codeup/[BFS_DFS]4503_바이러스.txt",'r')

def solution():
    st = [1]
    cnt = 0
    visited[1] = True
    while(st) :
        warm = st.pop(0)

        if warm in gp :
            tmp = gp[warm]
            for i in tmp :
                if visited[i] == False :
                    st.append(i)
                    visited[i] = True
                    cnt += 1

    return cnt


T = int(input())
for _ in range(T):
    n = int(input())
    s = int(input())
    visited = [False for _ in range(n+1)]
    gp = {}

    for _ in range(s) :
        a, b = map(int, input().split())
        if a in gp :
            gp[a] += [b]
        else :
            gp[a] = [b]

        if b in gp :
            gp[b] += [a]
        else :
            gp[b] = [a]
    print(solution())
