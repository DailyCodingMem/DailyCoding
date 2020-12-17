# baekjoon - [19238]스타트택시 (2020-12-17)
# https://www.acmicpc.net/problem/19238

import sys
from collections import deque
sys.stdin = open("baekjoon/[19238]스타트택시.txt",'r')

def nearbyCustomer(y,x) :
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    num, dist = 9999999, 9999999

    for i in range(len(cust)) :
        visited = [[False for _ in range(N)] for _ in range(N)]
        que = deque([(y, x, 0)])
        visited[y][x] = True
        cy, cx = cust[i][1]

        while(que) :
            uy, ux, cnt = que.popleft()

            if (cy, cx) == (uy, ux) :
                if cnt == dist :
                    num = min(num, cust[i][0])
                if cnt < dist :
                    num = cust[i][0]
                    dist = cnt                
                break


            for j in range(4) :
                ny = uy + dy[j]
                nx = ux + dx[j]

                if 0 <= ny < N and 0 <= nx < N :
                    if mat[ny][nx] == 0 and visited[ny][nx] == False :
                        que.append([ny,nx,cnt+1])
                        visited[ny][nx] = True

    return num, dist

def destination(num, dist) :    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    que = deque()
    des_y, des_x = 0,0
    visited = [[False for _ in range(N)] for _ in range(N)]
    idx = 0
    # print(num, cust)
    for i in range(len(cust)) :
        if cust[i][0] == num : 
            tmp_y, tmp_x = cust[i][1]

            que.append((tmp_y,tmp_x, dist))
            des_y, des_x = cust[i][2]
            idx = i
    del cust[idx]

    while(que) :
        y, x, cnt= que.popleft()
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N :
                if mat[ny][nx] == 0 and visited[ny][nx] == False :
                    que.append((ny,nx,cnt+1))
                    visited[ny][nx] = True
                    if (ny, nx) == (des_y, des_x) :
                        return ny, nx, cnt + 1
    
    return 9999999




        





T = int(input())
for t in range(1, T+1):
    N, M, O = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    cust = deque()
    for m in range(M) :
        sy, sx, fy, fx = map(int, input().split())
        cust.append([m, (sy-1,sx-1), (fy-1,fx-1)])

    check = [False for _ in range(N)]
    posible = True
    for _ in range(M) :
        num, dist = nearbyCustomer(y,x)
        # print(dist)
        if num == 9999999 :
            posible = False
            # print("출")
            break
        y, x, spend_oil = destination(num, dist)
        # print(spend_oil)
        if O - spend_oil < 0 :
            posible = False
            # print("오")
            break
        else :
            O = O - spend_oil + (spend_oil-dist) * 2
    if posible :
        print(O)
    else :
        print(-1)


