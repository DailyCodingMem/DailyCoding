# codeup - 스택 - 거꾸로출력하기3 (2020-09-14)
# https://codeup.kr/problem.php?id=1402

import sys
sys.stdin = open("codeup/[스택]1402_거꾸로출력하기3.txt",'r')

T = int(input())
for _ in range(T):
    n = int(input())
    st = list(map(int, input().split()))

    for i in range(n):
        print(st.pop(),end=" ")