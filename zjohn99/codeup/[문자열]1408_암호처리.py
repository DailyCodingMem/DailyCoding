# codeup - 문자열 - 암호처리 (2020-09-07)
# https://codeup.kr/problem.php?id=1408

import sys
sys.stdin = open("codeup/[문자열]1408_암호처리.txt",'r')

T = int(input())
for _ in range(T):
    text = input()
    encryption1 = ''
    encryption2 = ''

    for t in text:
        encryption1 += chr(ord(t) + 2)
        encryption2 += chr(((ord(t)*7) % 80 +48))

    print(encryption1)
    print(encryption2)
