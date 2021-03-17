# baekjoon - [1949]우수마을 (2021-01-23)
# https://www.acmicpc.net/problem/1949

import sys
from collections import deque
sys.stdin = open("baekjoon/[1949]우수마을.txt",'r')
# 생각한 방법
# 1. 조합을 해서 1개 부터 쭉 계산 - 터질듯
# 2. 노드가 1개인 애들을 후보군으로 놔두고 dfs 로 값을 저장


def DFS(current) :
    visited[current] = True
    s = [current]
    DP[current][0] = population[current]
    print(DP)
    print(s)
    while s:
        current = s[-1]
        for next in connection[current]:
            if not visited[next]:
                s.append(next)
                visited[next] = True
                DP[next][0] = population[next]
                break
 
        else:
            s.pop()
            if s:
                DP[s[-1]][0] += DP[current][1]
                DP[s[-1]][1] += max(DP[current][0], DP[current][1])
            else :
                print(s)
                print('dddddd')

    print(DP)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    population = [0] + list(map(int,input().split()))
    connection = [[] for _ in range(N+1)]
    for i in range(N-1):
        a, b = map(int,input().split())
        connection[a].append(b)
        connection[b].append(a)
    
    DP = [[0, 0] for _ in range(N+1)]
    visited = [False] * (N+1)
    DFS(1)
    print(max(DP[1][0], DP[1][1]))
    
        
    # https://cotak.tistory.com/29