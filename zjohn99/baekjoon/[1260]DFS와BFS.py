# baekjoon - [1260]DFS와BFS (2020-12-08)
# https://www.acmicpc.net/problem/1260
import sys
from collections import deque
sys.stdin = open("baekjoon/[1260]DFS와BFS.txt",'r')

def DFS(idx):  
    global visited_dfs
    print(idx, end=" ")
    if idx in dic :
        for val in dic[idx] :
            if visited_dfs[val] == False :
                visited_dfs[val] = True
                DFS(val)
def BFS():
    visited = [False for _ in range(N+1)]
    que = deque([V])
    visited[V] = True
    while(que) :
        x = que.popleft()
        if x in dic :
            for val in dic[x] :
                if visited[val] == False :
                    que.append(val)
                    visited[val] = True

        print(x, end=" ")

T = int(input())
for t in range(1, T+1):
    N, M, V = map(int, input().split())
    dic = {}
    for _ in range(M) :
        a, b = map(int, input().split())
        if a in dic :
            dic[a] += [b]
        else :
            dic[a] = [b]
        if b in dic :
            dic[b] += [a]
        else :
            dic[b] = [a]
    for key in dic.keys():
        dic[key].sort()
    visited_dfs = [False for _ in range(N+1)]
    visited_dfs[V] = True
    DFS(V)
    print()
    BFS()
    print()