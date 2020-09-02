# codeup - 문자열 - 알파벳대소문자변환 (2020-09-02)
# https://codeup.kr/problem.php?id=1295

import sys
sys.stdin = open("codeup/[문자열]1295_알파벳대소문자변환.txt",'r')

T = int(input())
for _ in range(T):
    words = input()
    words = words.swapcase()
    # swapcase() => 대문자는 소문자로 소문자는 대문자로

    print(words)