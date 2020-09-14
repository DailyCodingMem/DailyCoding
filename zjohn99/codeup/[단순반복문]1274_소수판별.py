# codeup - 단순반복 - 소수판별 (2020-09-04)
# https://codeup.kr/problem.php?id=1274

import sys
sys.stdin = open("codeup/[단순반복문]1274_소수판별.txt",'r')

T = int(input())
for _ in range(T):
    number = int(input())

    for i in range(1,number) :
        if i > 1 and number%i == 0:
            print("not prime")
            break
    else:
        print("prime")
            
