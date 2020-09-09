# codeup - 문자열 - IOI (2020-09-09)
# https://codeup.kr/problem.php?id=1733

import sys
sys.stdin = open("codeup/[문자열]1733_IOI.txt",'r')

T = int(input())
for _ in range(T):
    word = input()
    if word == 'IOI':
        print("IOI is the International Olympiad in Informatics.")
    else :
        print("I don't care.")