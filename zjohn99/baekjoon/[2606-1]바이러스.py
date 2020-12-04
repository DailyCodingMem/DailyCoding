# baekjoon - [2606]바이러스 (2020-12-18)
# https://www.acmicpc.net/problem/2606
import sys
from collections import deque
sys.stdin = open("baekjoon/[2606]바이러스.txt",'r')

def solution() :
    visited = [False for _ in range(N+1)]
    que = deque([1])
    visited[1] = True
    cnt = 0
    while(que) :
        x = que.popleft()

        for i in dic[x]:
            if visited[i] == False :
                visited[i] = True
                que.append(i)
                cnt += 1

    return cnt



T = int(input())
for t in range(1, T+1):
    N = int(input())
    S = int(input())
    dic = {}

    for s in range(S) :
        a, b = map(int, input().split())
        if a in dic :
            dic[a] += [b]
        else :
            dic[a] = [b]
        
        if b in dic :
            dic[b] += [a]
        else :
            dic[b] = [a]

    print(solution())
        
