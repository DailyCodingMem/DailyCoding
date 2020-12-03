# baekjoon - [1697]숨바꼭질 (2020-12-03)
# https://www.acmicpc.net/problem/1697

import sys
sys.stdin = open("baekjoon/[1697]숨바꼭질.txt",'r')

def solution():
    visited = [0 for _ in range(2000001)]

    que = [N]
    cnt = 0
    while(que) :
        x = que.pop(0)
        if x == K :
            return 0

        for i in (x-1, x+1, x*2):
            if 0 <= i <= 2000000 :
                if i == K :
                    return visited[x] + 1
                if visited[i] == 0 :
                    visited[i] = visited[x] + 1
                    que.append(i)
                
T = int(input())
for t in range(1, T+1):
   N, K = map(int, input().split())

   print(solution())