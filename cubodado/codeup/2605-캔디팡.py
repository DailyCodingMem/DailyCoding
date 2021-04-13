from collections import deque

arr = [list(map(int, input().split())) for _ in range(7)]
deque = deque()
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
cnt = 0

for a in range(len(arr)):
    for b in range(len(arr)):
        if a == len(arr) -1 and b == len(arr) -1:
            break
        if arr[a][b] != 0:
            deque.append((a,b))
            check = arr[a][b]
            arr[a][b] = 0
            path = 1
            while deque:
                y, x = deque.popleft()
                for i in range(4):
                    newY = y + dy[i]
                    newX = x + dx[i]
                    if 0 <= newY < len(arr) and 0 <= newX < len(arr) and check == arr[newY][newX]:
                        arr[newY][newX] = 0
                        deque.append((newY, newX))
                        path += 1
            if 3 <= path:
                cnt += 1

print(cnt)
