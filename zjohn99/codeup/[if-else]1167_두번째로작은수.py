# codeup - if_else - 두번째로 작은수 (2020-09-04)
# https://codeup.kr/problem.php?id=1167

import sys
sys.stdin = open("codeup/[if-else]1167_두번째로작은수.txt",'r')

T = int(input())
for _ in range(T):
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(numbers[1])