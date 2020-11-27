# programmers - Lv4 - 게임맵최단거리 (2020-10-17)
# https://programmers.co.kr/learn/courses/30/lessons/1844
# bfs

from collections import deque
import sys
sys.stdin = open("programmers/[Lv4]게임맵최단거리.txt",'r')

def solution(maps):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    # visited = [[False for _ in range(M)] for _ in range(N)]
    answer = 0
    fin_y, fin_x = N-1, M-1
    
    que = deque()
    que.append((0,0,answer+1))
    # visited[0][0] = True
    maps[0][0] = 0
    while(que) :
        y, x, dep = que.pop()

        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M : # inner
                # if visited[ny][nx] == False and maps[ny][nx] == 1 :
                if maps[ny][nx] == 1 :
                    if (ny, nx) == (fin_y, fin_x) :
                        answer = dep + 1
                        return answer
                    que.append((ny, nx, dep+1))
                    maps[ny][nx] = 0
                    # visited[ny][nx] = True

    answer = -1
    return answer


T = int(input())
for _ in range(T):
    N, M = 5, 5
    maps = [list(map(int, input().split())) for _ in range(N)]

    print(solution(maps))    

