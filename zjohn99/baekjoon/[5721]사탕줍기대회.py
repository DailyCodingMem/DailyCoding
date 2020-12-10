# baekjoon - [5721]사탕줍기대회 (2020-12-10)
# https://www.acmicpc.net/problem/5721
import sys
sys.stdin = open("baekjoon/[5721]사탕줍기대회.txt",'r')


T = int(input())
for t in range(1, T+1):
    while(True) :    
        M, N = map(int, input().split())
        if (M, N) == (0,0) :
            break
        mat = [list(map(int, input().split())) for _ in range(M)]
        
