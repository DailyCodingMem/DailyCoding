# codeup - 문자열 - 큰수비교 (2020-09-10)
# https://codeup.kr/problem.php?id=1754

import sys
sys.stdin = open("codeup/[문자열]1754_큰수비교.txt",'r')

T = int(input())
for _ in range(T):
    a,b = map(int, input().split())
    
    if a > b:
        print(b, end=" ")
        print(a)
    else :
        print(a, end=" ")
        print(b)