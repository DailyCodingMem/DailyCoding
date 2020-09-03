# codeup - 단순반복문 - 기부 (2020-09-03)
# https://codeup.kr/problem.php?id=1272

import sys
sys.stdin = open("codeup/[단순반복문]1272_기부.txt",'r')

def check(num):
    result = 0
    if num%2 == 0: # 짝수이면,
        result = num//2 * 10
    else : # 홀수이면,
        result = num//2 + 1
    return result


T = int(input())
for _ in range(T):
    k,h = map(int, input().split())
    print(check(k)+check(h))
    