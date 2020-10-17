grimpan = [list(input())for _ in range(10)]
x,y = map(int,input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def drawing(y,x):
    grimpan[y][x] = '*'
    for i in range(4):
        Y = y + dy[i]
        X = x + dx[i]
        if 0 <= X < 10 and 0 <= Y < 10 and grimpan[Y][X] == '_':
            grimpan[Y][X] = '*'
            drawing(Y,X)
if grimpan[y][x] == '_':
    drawing(y,x)
for i in range(10):
    print("".join(grimpan[i]))