# baekjoon - [1987]알파벳 (2020-12-15)
# https://www.acmicpc.net/problem/1987

from collections import deque
import sys
sys.stdin = open("baekjoon/[1987]알파벳.txt",'r')

def solution(y, x, cnt) :
    global ans

    ans = max(ans, cnt)

    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C and not alpha[ord(mat[ny][nx]) - 65] :
            alpha[ord(mat[ny][nx]) - 65] = 1
            solution(ny, nx, cnt + 1)
            alpha[ord(mat[ny][nx]) - 65] = 0


T = int(input())
for t in range(1, T+1):
    R, C = map(int, input().split())
    mat = [list(map(str,input())) for _ in range(R)]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    alpha = [0] * 26
    alpha[ord(mat[0][0]) - 65] = 1
    ans = 1

    solution(0,0,1)

    print(ans)