# codeup - if_else - 윤년판별 (2020-09-03)
# https://codeup.kr/problem.php?id=1166

import sys
sys.stdin = open("codeup/[if-else]1166_윤년판별.txt",'r')

T = int(input())
for _ in range(T):
    year = int(input())
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        print("yes")
    else:
        print("no")