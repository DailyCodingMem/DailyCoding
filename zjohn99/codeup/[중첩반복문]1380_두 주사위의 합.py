# codeup - 중첩반복문 - 두주사위의합 (2020-09-08)
# https://codeup.kr/problem.php?id=1380

import sys
sys.stdin = open("codeup/[중첩반복문]1380_두 주사위의 합.txt",'r')

T = int(input())
for _ in range(T):
    sum_val = int(input())
    for i in range(1, 7):
        if sum_val- i> 0 and sum_val-i < 7:
            print(i, end=" ")
            print(sum_val-i)