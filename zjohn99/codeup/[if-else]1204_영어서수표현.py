# codeup - if_else - 영어서수표현 (2020-09-10)
# https://codeup.kr/problem.php?id=1204

import sys
sys.stdin = open("codeup/[if-else]1204_영어서수표현.txt",'r')

T = int(input())
for _ in range(T):
    val = int(input())

    tmp = val % 10
    if tmp == 1:
        if val == 11 :
            print("{}th".format(val))
        else:
            print("{}st".format(val))
    elif tmp == 2:
        if val == 12 :
            print("{}th".format(val))
        else :
            print("{}nd".format(val))
    elif tmp == 3:
        if val == 13 :
            print("{}th".format(val))
        else :
            print("{}rd".format(val))
    else:
        print("{}th".format(val))