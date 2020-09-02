# codeup - if_else - 터널통과하기1 (2020-09-02)
# https://codeup.kr/problem.php?id=1164

import sys
sys.stdin = open("codeup/[if-else]1164_터널통과하기1.txt",'r')

T = int(input())
for _ in range(T):
    h_tunnel = list(map(int, input().split()))
    car = 170
    for t in h_tunnel:
        if t <= car:
            print("CRASH")
            break
    else:
        print("PASS")