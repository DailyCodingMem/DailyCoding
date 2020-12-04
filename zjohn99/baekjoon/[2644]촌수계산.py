# baekjoon - [2644]촌수계산 (2020-12-04)
# https://www.acmicpc.net/problem/2644
import sys
from collections import deque
sys.stdin = open("baekjoon/[2644]촌수계산.txt",'r')

def solution(p1,p2) :
    if p1 == p2 :
        return 0
    st = deque()
    st.append((p1,0))
    while(st) :
        x,cnt = st.popleft()
        for i in range(n+1) :
            if fam[x][i][0] == 1 and fam[x][i][1] == 0 :
                fam[x][i] = (1, cnt+1)
                fam[i][x] = (1, cnt+1)
                st.append((i,fam[x][i][1]))
                if i == p2 :
                    return fam[x][i][1]
    else :
        return -1


T = int(input())
for t in range(1, T+1):
    n = int(input())
    p1, p2 = map(int, input().split())
    m = int(input())
    fam = [[(0,0) for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(m):
        X, Y = map(int, input().split())
        fam[X][Y] = (1,0)    
        fam[Y][X] = (1,0)

    print(solution(p1,p2))        
