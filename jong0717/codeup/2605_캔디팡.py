def candypang(y,x):
    global cnt, pangcnt
    cnt += 1
    visited[y][x] = 1
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < 7 and 0 <= Y < 7:
            if candy[y][x] == candy[Y][X]:
                if not visited[Y][X]:
                    candypang(Y,X)
                    if cnt >= 3:
                        cnt = 0
                        pangcnt += 1

candy = [list(map(int,input().split()))for _ in range(7)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[0 for _ in range(7)]for _ in range(7)]
pangcnt = 0
for i in range(7):
    for j in range(7):
        if not visited[j][i]:
            cnt = 0
            candypang(j,i)
print(pangcnt)
