# baekjoon - [2075]N번째큰수 (2021-01-25)
# https://www.acmicpc.net/problem/2075
import sys
from heapq import *
sys.stdin = open("baekjoon/[2075]N번째큰수.txt",'r')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    
    mat = list(input().split() for _ in range(N))
    print(mat)
    