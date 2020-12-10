# baekjoon - [11403]경로찾기 (2020-12-10)
# https://www.acmicpc.net/problem/11403
import sys
from collections import deque
from pprint import pprint
sys.stdin = open("baekjoon/[11403]경로찾기.txt",'r')

def solution(x) :
    que = deque([x])
    visited = [0 for _ in range(N)]

    while(que) :
        nx = que.popleft()
        for i in range(N) :
            if visited[i] == 0 and mat[nx][i] == 1 :
                visited[i] = 1
                que.append(i)
                
    result.append(visited)

T = int(input())
for _ in range(T) :
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    result = []

    for i in range(N) :
        solution(i)
    
    for i in range(N) :
        for j in range(N) :
            print(result[i][j], end=' ')
        print()