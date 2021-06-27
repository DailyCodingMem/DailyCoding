def solution(N, mine):
    arr = [[0]*N for _ in range(N)]

    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,-1,0,1]

    for m in mine:
        Y, X = m[0]-1, m[1]-1
        arr[Y][X] = -1
        for i in range(8):
            checkY = Y + dy[i]
            checkX = X + dx[i]
            if 0 <= checkY < N and 0 <= checkX < N and arr[checkY][checkX] != -1:
                arr[checkY][checkX] += 1
    return arr

N = 9
mine = [[1, 1], [1, 7], [2, 7], [3, 6], [4, 1], [4, 4], [4, 8], [8, 4], [8, 5], [9, 6]]
arr = [[0]*N for _ in range(N)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for m in mine:
    Y, X = m[0]-1, m[1]-1
    arr[Y][X] = -1
    for i in range(8):
        checkY = Y + dy[i]
        checkX = X + dx[i]
        if 0 <= checkY < N and 0 <= checkX < N and arr[checkY][checkX] != -1:
            arr[checkY][checkX] += 1
print(arr)
