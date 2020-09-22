from collections import deque

W, H = map(int, input().split())
arr = [list(input().split()) for _ in range(H)]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
dx = [1, -1, 0, 0, -1, 1, 1, -1]
stack = deque()
cnt = 0

for a in range(H):
    for b in range(W):
        if arr[a][b] == 'L':
            stack.append((a,b))
            arr[a][b] = '.'
            while stack:
                y, x = stack.popleft()
                for i in range(8):
                    newY = y + dy[i]
                    newX = x + dx[i]
                    if 0 <= newY < H and 0 <= newX < W and arr[newY][newX] == 'L':
                        stack.append((newY,newX))
                        arr[newY][newX] = '.'
            cnt += 1

print(cnt)