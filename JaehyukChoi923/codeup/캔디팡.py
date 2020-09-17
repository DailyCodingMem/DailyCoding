def dfs(y, x):
    global cnt, pcnt
    cnt += 1
    visited[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 7 and 0 <= ny < 7:
            if arr[y][x] == arr[ny][nx]:
                if not visited[ny][nx]:
                    dfs(ny, nx)
                    if cnt >= 3:
                        cnt = 0
                        pcnt += 1

arr = []
for _ in range(7):
    arr.append(list(map(int, input().split())))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0 for _ in range(7)] for _ in range(7)]

pcnt = 0
for i in range(7):
    for j in range(7):
        if not visited[j][i]:
            cnt = 0
            dfs(j, i)
print(pcnt)
