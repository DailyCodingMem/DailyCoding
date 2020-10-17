field = [list(map(int,input().split())) for _ in range(9)]
r,c = map(int,input().split())
dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]
r -= 1
c -= 1
bomb = [list('_' for _ in range(9))for _ in range(9)]
def Mine(y,x):
    mines = 0
    for i in range(8):
        Y = y + dy[i]
        X = x + dx[i]
        if 0 <= X < 9 and 0 <= Y < 9 and field[Y][X]:
            mines += 1
    bomb[y][x] = mines
    if not mines:
        for i in range(8):
            Y = y + dy[i]
            X = x + dx[i]
            if 0 <= X < 9 and 0 <= Y < 9 and bomb[Y][X] == '_':
                Mine(Y,X)
if field[r][c]:
    bomb[r][c] = -1
else:
    Mine(r,c)
for i in range(9):
    for j in range(9):
        print(bomb[i][j],end=' ')
    print()