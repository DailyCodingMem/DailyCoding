# codeup - if_else - 만능휴지통 (2020-09-09)
# https://codeup.kr/problem.php?id=1180

import sys
sys.stdin = open("codeup/[if-else]1180_만능휴지통.txt",'r')

T = int(input())
for _ in range(T):
    trash = int(input())
    tmp = ((trash%10)*10 + (trash//10)) * 2
    if tmp > 100 :
        tmp = tmp % 100
    if tmp > 50 :
        print(tmp)
        print("OH MY GOD")
    else :
        print(tmp)
        print("GOOD")
