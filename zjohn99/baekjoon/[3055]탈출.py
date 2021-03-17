# baekjoon - [3055]탈출 (2020-12-14)
# https://www.acmicpc.net/problem/3055
import sys
from collections import deque 
from pprint import pprint
sys.stdin = open("baekjoon/[3055]탈출.txt",'r')

def solution() :
    global water
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[False for _ in range(C)] for _ in range(R)]
    que = deque(S)
    tmpY, tmpX, tmpCnt = S[0]
    visited[tmpY][tmpX] = True
    while(True) :
        nQue = deque()
        sink()
        while(que) :
            y,x,cnt = que.popleft()
            


            for i in range(4) :
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < R and 0 <= nx < C :
                    if mat[ny][nx] == '.' and visited[ny][nx] == False:
                        nQue.append((ny,nx,cnt+1))
                        visited[ny][nx] = True

                    if mat[ny][nx] == 'D' :
                        return cnt+1
        que = nQue
        if len(nQue) == 0 :
            return 'KAKTUS'


def sink() :
    global water

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    nWater = deque()

    while(water) :
        y,x = water.popleft()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < R and 0 <= nx < C :
                if mat[ny][nx] == '.' :
                    mat[ny][nx] = '*'
                    nWater.append((ny,nx))
    water = nWater



T = int(input())
for t in range(1, T+1):
    R, C = map(int, input().split())
    mat = [list(map(str, input())) for _ in range(R)]
    water = deque()
    S = []
    D = []
    for i in range(R) :
        for j in range(C) :
            if mat[i][j] == '*' :
                water.append((i,j))
            if mat[i][j] == 'D' :
                D.append((i,j))
            if mat[i][j] == 'S' :
                S.append((i,j,0))

    print(solution())




