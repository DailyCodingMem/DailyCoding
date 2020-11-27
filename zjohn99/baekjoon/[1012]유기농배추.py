# baekjoon - [1012]유기농배추 (2020-10-17)
# https://www.acmicpc.net/problem/1012
import sys
from pprint import pprint
sys.stdin = open("baekjoon/[1012]유기농배추.txt",'r')

def solution(y, x) :
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    que = [(y,x)]
    mat[y][x] = 0
    while(que) :
        y,x = que.pop()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M :
                if mat[ny][nx] == 1 :
                    que.append((ny,nx))
                    mat[ny][nx] = 0
    


T = int(input())
for t in range(1, T+1):
    M, N, K = map(int, input().split())

    mat = [[0 for _ in range(M)] for _ in range(N)]
    B = []
    cnt = 0
    for k in range(K) :
        pos_x, pos_y = map(int, input().split())
        B.append((pos_y,pos_x))
        mat[pos_y][pos_x] = 1
    
    for b in B :
        pos_y, pos_x = b
        if mat[pos_y][pos_x] == 1 :
            solution(pos_y, pos_x)
            cnt += 1

    print(cnt)
