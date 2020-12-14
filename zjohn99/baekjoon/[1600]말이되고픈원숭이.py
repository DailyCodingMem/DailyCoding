# baekjoon - [1600]말이되고픈원숭이 (2020-12-10)
# https://www.acmicpc.net/problem/1600
import sys
from collections import deque
sys.stdin = open("baekjoon/[1600]말이되고픈원숭이.txt",'r')

def solution() :
    dy = [0, -1, 0, 1, 1, 2, 2, 1]
    dx = [1, 0, -1, 0, 2, 1, -1, -2]
    visited = [[0 for _ in range(W)] for _ in range(H)]

    que = deque([(0,0,K,0)]) # y,x,K,cnt
    # visited[0][0] = 0
    if (0,0) == (H-1,W-1)  :
        return 0

    while(que) :
        y,x,k,cnt = que.popleft()
        
        jump = 0

        if k > 0 : # K 번 남았을 때,
            jump = 8
        else : # 말처럼 다 뛰었을 때,
            jump = 4
        
        for i in range(jump) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < H and 0 <= nx < W :
                if mat[ny][nx] == 0:
                    # if visited[ny][nx] > cnt+1 :
                    if i >= 4 :
                        que.append((ny,nx,k-1,cnt+1))
                    else :
                        que.append((ny,nx,k,cnt+1))
                    visited[ny][nx] = cnt+1

                    if (ny,nx) == (H-1,W-1) :
                        return cnt+1
    return -1

T = int(input())
for t in range(1, T+1):
    K = int(input())
    W, H = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(H)]
    print(solution())