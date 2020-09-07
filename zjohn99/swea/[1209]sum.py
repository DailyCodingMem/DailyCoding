# swea - [1209]sum (2020-09-07)
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq

import sys
sys.stdin = open("swea/[1209]sum.txt",'r')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    mat = [list(map(int, input().split())) for _ in range(100)]
    rl_val = 0
    lr_val = 0
    col_val = [0 for _ in range(100)]
    row_val = [0 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            row_val[i] += mat[i][j]
            col_val[j] += mat[i][j]
            if i == j :
                lr_val += mat[i][j]
            if i+j+1 == 100 :
                rl_val += mat[i][j]
    max_val = max(rl_val, lr_val, max(row_val), max(col_val))
    print("#{0} {1}".format(t, max_val))
