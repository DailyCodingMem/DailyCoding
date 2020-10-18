# baekjoon - [1753]최단경로 (2020-10-17)
# https://www.acmicpc.net/problem/1753
import sys
sys.stdin = open("baekjoon/[1753]최단경로.txt",'r')

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    K = int(input())
    u,v,w = map(int, input().split())


    visited = [False for _ in range(V)]

       
