arr = [list(map(int, input().split(' '))) for _ in range(10)]
stack = []
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
drawings = 0

for a in range(10):
    for b in range(10):
        if arr[a][b] == 1:
            stack.append((a,b))
            arr[a][b] = 0

            while stack:
                y,x = stack.pop()
                for i in range(4):
                    newY = y + dy[i]
                    newX = x + dx[i]
                    if 0 <= newY < 10 and 0 <= newX < 10 and arr[newY][newX] == 1:
                        arr[newY][newX] = 0
                        stack.append((newY,newX))

            drawings += 1

print(drawings)