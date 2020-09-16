# codeup - BFS/DFS - 배수 (2020-09-15)
# https://codeup.kr/problem.php?id=2102
# 가장작은 자연수 -> bfs로 풀기
# 시간초과....

import sys
sys.stdin = open("codeup/[BFS_DFS]2102_배수.txt",'r')                     

def solution():
    dn = ['0','1']
    result = ['1']

    while(result):
        tmp = result.pop(0)
        if int(tmp) % N == 0 :
            return tmp
        for i in dn:
            if int(tmp+i) % N == 0:
                return tmp+i
            else:
                result.append(tmp+i)


T = int(input())
for _ in range(T):
    N = int(input())

    print(solution())
   
