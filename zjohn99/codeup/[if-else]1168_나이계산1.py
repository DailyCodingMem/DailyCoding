# codeup - if_else - 나이계산1 (2020-09-07)
# https://codeup.kr/problem.php?id=1168

import sys
sys.stdin = open("codeup/[if-else]1168_나이계산1.txt",'r')

T = int(input())
for _ in range(T):
    id_bir, id_sex = input().split()
    base_year = 14
    if int(id_sex) > 2: # 00년생들
        print(base_year - int(id_bir[0:2]) - 1)
    else :
        print(base_year + 100-int(id_bir[0:2]) - 1)
