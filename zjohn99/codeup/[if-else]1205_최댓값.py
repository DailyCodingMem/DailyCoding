# codeup - if_else - 최댓값 (2020-09-11)
# https://codeup.kr/problem.php?id=1205

import sys
import math
sys.stdin = open("codeup/[if-else]1205_최댓값.txt",'r')

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    result = [a+b, a-b, b-a, a*b, a/b, b/a, math.pow(a,b), math.pow(b,a)]
    tmp = float(max(result))
    print("%0.6f" %tmp)