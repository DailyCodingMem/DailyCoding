# codeup - if_else - 30분전 (2020-09-08)
# https://codeup.kr/problem.php?id=1173

import sys
sys.stdin = open("codeup/[if-else]1173_30분전.txt",'r')

T = int(input())
for _ in range(T):
    clock = list(map(int, input().split()))
    if clock[1] - 30 < 0 :
        clock[1] = 60 - (30 - clock[1])
        if clock[0] - 1 < 0 :
            clock[0] = 23
        else :
            clock[0] -= 1
    else :
        clock[1] -= 30
    print(clock[0], end=' ')
    print(clock[1])


