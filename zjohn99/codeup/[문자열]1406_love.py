# codeup - 문자열 - love (2020-09-03)
# https://codeup.kr/problem.php?id=1406

import sys
sys.stdin = open("codeup/[문자열]1406_love.txt",'r')

T = int(input())
for _ in range(T):
    words = input()
    if words == 'love':
        print("I love you.")