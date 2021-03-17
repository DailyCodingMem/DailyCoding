# baekjoon - [11724]연결요소의개수 (2020-12-09)
# https://www.acmicpc.net/problem/11724
import sys
from collections import deque
sys.stdin = open("baekjoon/[11724]연결요소의개수.txt",'r')

def solution() :
    visited = [0 for _ in range(N+1)]
    que = deque()
    cnt = 0
    for key in dic.keys() :
        if visited[key] == 0 :
            que.append(key)
            cnt += 1
            visited[key] = cnt
        while(que) :
            x = que.popleft()
            for val in dic[x] :
                if visited[val] == 0 :
                    que.append(val)
                    visited[val] = cnt

    for i in range(1, N+1) :
        if visited[i] == 0 :
            cnt += 1
    return cnt

# def solution() :
#     visited = [0 for _ in range(N+1)]
#     que = deque()
#     cnt = 0
#     for i in range(1, N+1) :
#         if visited[i] == 0 :
#             que.append(i)
#             cnt += 1
#             visited[i] = cnt
#         while(que) :
#             x = que.popleft()
#             if x in dic :
#                 for val in dic[x] :
#                     if visited[val] == 0 :
#                         que.append(val)
#                         visited[val] = cnt
    
#     return cnt

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    dic = {}

    for _ in range(M) :
        u,v = map(int, input().split())
        if u in dic :
            dic[u] += [v]
        else :
            dic[u] = [v]
        if v in dic :
            dic[v] += [u]
        else :
            dic[v] = [u]

    print(solution())