from collections import deque
def bfs(y, x):
    q = deque()
    visited[y][x] = 1
    q.append([x, y])
    if arr[y][x] == '*':
        q.popleft()
    while q:
        tx, ty = q.popleft()
        arr[ty][tx] = '*'
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < 10 and 0 <= ny < 10:
                if arr[ny][nx] == '_':
                    if not visited[ny][nx]:
                        q.append([nx, ny])

arr = []
for _ in range(10):
    arr.append(list(input()))
x, y = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[0 for _ in range(10)] for _ in range(10)]
bfs(y, x)
for i in arr:
    print(''.join(i))
