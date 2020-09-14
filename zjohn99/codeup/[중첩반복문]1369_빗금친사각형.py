# codeup - 중첩반복문 - 빗금친사격형 (2020-09-10)
# https://codeup.kr/problem.php?id=1369

import sys
sys.stdin = open("codeup/[중첩반복문]1369_빗금친사각형.txt",'r')

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    for i in range(n):
        if i == 0 or i == n-1 :
            for j in range(n) :
                if j == n-1:
                    print("*")
                else:
                    print("*", end='')
        else :

            for j in range(n):
                if j == 0:
                    print("*", end='')
                elif j == n-1 :
                    print("*")
                elif (i+j+1) % k == 0 :
                    print("*", end='')

                else :
                    print(" ", end='')
