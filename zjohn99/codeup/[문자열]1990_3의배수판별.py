# codeup - 문자열 - 3의배수판별하기 (2020-09-11)
# https://codeup.kr/problem.php?id=1990

import sys
sys.stdin = open("codeup/[문자열]1990_3의배수판별.txt",'r')

T = int(input())
for _ in range(T):
    a = int(input())
    if a % 3 == 0 :
        print(1)
    else :
        print(0)