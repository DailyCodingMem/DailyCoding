# baekjoon - [2696]중앙값구하기 (2021-01-25)
# https://www.acmicpc.net/problem/2696
import sys
sys.stdin = open("baekjoon/[2696]중앙값구하기.txt",'r')


T = int(input())
for t in range(1, T+1):
    M = int(input())
    mat = list(map(int, input().split()))

    print(mat)

    