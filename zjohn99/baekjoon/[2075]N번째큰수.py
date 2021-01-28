# baekjoon - [2075]N번째큰수 (2021-01-25)
# https://www.acmicpc.net/problem/2075
import sys
from heapq import *
sys.stdin = open("baekjoon/[2075]N번째큰수.txt",'r')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = []
    for _ in range(N) :
        mat += list(map(int, input().split()))
    heapify(mat)
    while(len(mat) > N): 
        heappop(mat)


    print(heappop(mat))
   
    # for i in range(len(mat)) :
    #     mat[i] = -mat[i]
    
    # heapify(mat)
    # for i in range(N) :
    #     tmp = heappop(mat)
    #     if i == N-1 :
    #         print(-tmp)
    