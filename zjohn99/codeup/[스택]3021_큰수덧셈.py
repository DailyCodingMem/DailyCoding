# codeup - 스택 - 큰수덧셈 (2020-09-17)
# https://codeup.kr/problem.php?id=3021

import sys
sys.stdin = open("codeup/[스택]3021_큰수덧셈.txt",'r')

T = int(input())
for _ in range(T):
    a = int(input())
    b = int(input())
    print(a+b)