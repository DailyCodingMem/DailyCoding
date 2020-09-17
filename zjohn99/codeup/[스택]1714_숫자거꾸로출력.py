# codeup - 스택 - 숫자거꾸로출력 (2020-09-15)
# https://codeup.kr/problem.php?id=1714

import sys
sys.stdin = open("codeup/[스택]1714_숫자거꾸로출력.txt",'r')

T = int(input())
for _ in range(T):
    N = list(input())
    for i in range(len(N)-1, -1, -1):
        print(N[i],end="")