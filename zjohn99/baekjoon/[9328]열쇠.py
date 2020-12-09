# baekjoon - [9328]열쇠 (2020-12-09)
# https://www.acmicpc.net/problem/9328

import sys
from collections import deque
from copy import deepcopy
sys.stdin = open("baekjoon/[9328]열쇠.txt",'r')

def solution(y,x) :
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[False for _ in range(w)] for _ in range(h)]
    tmp_visite = deepcopy(visited)
    st = deque([(y,x)])
    visited[y][x] = True
    cnt = 0
    start_y, start_x = y,x
    while(st) :
        y, x = st[-1]

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < h and 0 <= nx < w :
                if visited[ny][nx] == False and mat[ny][nx] != '*' :
                    if 65 <= ord(mat[ny][nx]) <= 90 : # 문
                        if mat[ny][nx] not in key :
                            continue
                    elif 97 <= ord(mat[ny][nx]) <= 122 : # 열쇠
                        key.append(mat[ny][nx].upper())
                        mat[ny][nx] = '.'
                        st = deque([(start_y,start_x)])
                        visited = deepcopy(tmp_visite)
                        visited[start_y][start_x] = True
                        break
                    elif mat[ny][nx] == '$' :
                        cnt +=1
                        mat[ny][nx] = '.'
                    st.append((ny,nx))
                    visited[ny][nx] = True
                    break
        else :
            st.pop()

    return cnt

T = int(input())
for t in range(1, T+1):
    h, w = map(int, input().split())
    mat = [list(map(str, input())) for _ in range(h)]
    key = list(map(str, input()))
    door = []
    paper = 0
    if '0' in key :
        key.pop()
    else :
        for i in range(len(key)) :
            key[i] = key[i].upper()
            
    for i in range(h) :
        if i == 0 or i == h-1 :
            for j in range(w) :
                    if mat[i][j] == '.' or 97 <= ord(mat[i][j]) <= 122:
                        door.append((i,j))
        elif 0 < i < h-1 :
            if mat[i][0] == '.' or 97 <= ord(mat[i][0]) <= 122:
                door.append((i,0))
            if mat[i][w-1] == '.' or 97 <= ord(mat[i][w-1]) <= 122:
                door.append((i,w-1))

    for i in range(len(door)) :
        y,x = door[i]
        paper += solution(y,x)
    print(paper)