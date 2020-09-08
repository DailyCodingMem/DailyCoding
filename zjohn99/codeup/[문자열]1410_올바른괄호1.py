# codeup - 문자열 - 올바른괄호1 (2020-09-08)
# https://codeup.kr/problem.php?id=1410

import sys
sys.stdin = open("codeup/[문자열]1410_올바른괄호1.txt",'r')

T = int(input())
for _ in range(T):
    word = input()
    l_open = 0
    r_open = 0

    for w in word:
        if w == "(":
            l_open += 1
        else :
            r_open += 1

    print(l_open, end=" ")
    print(r_open)