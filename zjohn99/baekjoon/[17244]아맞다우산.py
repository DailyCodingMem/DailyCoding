# baekjoon - [17244]아맞다우산 (2021-01-20)
# https://www.acmicpc.net/problem/17244
import sys
from collections import deque
from pprint import pprint
from copy import deepcopy
sys.stdin = open("baekjoon/[17244]아맞다우산.txt",'r')

def solution(item) :
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    cnt = 0

    for i in range(len(item)-1) :
        s = item[i]
        e = item[i+1]
        visited = [[False for _ in range(N)] for _ in range(M)]
        y, x = s
        val = 0
        visited[y][x] = True
        que = deque([(y,x,val)])
        check = True
        while(check) :
            y, x, val = que.popleft()

            for j in range(4) : 
                ny = y + dy[j]
                nx = x + dx[j]

                if 0 <= ny < M and 0 <= nx < N :
                    if mat[ny][nx] != '#' and visited[ny][nx] == False :
                        que.append((ny, nx, val+1))
                        visited[ny][nx] = True

                if e == (ny,nx) :
                    check = False
                    cnt += val+1
                    break
    return cnt

def perm(arr, s, e) :
    global len_items

    if s == e :
        tmp = deepcopy(arr) # 이부분을 어떻게 해야할까 그냥 append를 하면 같은 주소라서 바뀌어버림
        all_items.append(tmp)
        len_items += 1
        return
    
    for idx in range(s, e) :
        arr[idx], arr[s] = arr[s], arr[idx]
        perm(arr, s+1, e)
        arr[idx], arr[s] = arr[s], arr[idx]


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    mat = [list(input()) for _ in range(M)]
    start = []
    end = []
    items = []

    for i in range(M) :
        for j in range(N) :
            if mat[i][j] == 'S' :
                start.append((i,j))
            elif mat[i][j] == 'X' :
                items.append((i,j))
            elif mat[i][j] == 'E' :
                end.append((i,j))
    items = start + items + end 
    all_items = []
    len_items = 0
    perm(items, 1, len(items)-1)

    results = [0 for _ in range(len_items)]
    
    for i in range(len_items) :
        results[i] = solution(all_items[i])

    print(min(results))