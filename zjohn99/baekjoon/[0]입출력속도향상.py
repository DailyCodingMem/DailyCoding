# import sys
# sys.stdin = open("baekjoon/리스트회전.txt",'r')

    
# T = int(input())
# for t in range(1, T+1):

###########################################
# 첫째,  
# n = int(input()) # 이것보다는

from sys import stdin
n = int(stdin.readline()) # 이게 더 빠르다.

# print(n)

## 둘째,
# mat = list(map(int, input().split())) # 이것보다는
n, m = map(int, stdin.readline().split())
mat = [list(map(int, stdin.readline().split())) for _ in range(n)]

print(n, m)
print(mat)
