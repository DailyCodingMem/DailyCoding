import sys
sys.stdin = open("14500in.txt",'r')

import sys
dy = [-1,1,0,0]
dx = [0,0,-1,1]
n,m = map(int,sys.stdin.readline().split())
li = list(list(map(int,sys.stdin.readline().split())) for _ in range(n))

def tetris(newY,newX,res,cnt):
    global ans
    if cnt ==4:
        if res > ans:
            ans = res
            return
    for i in range(4):
        checkY = newY+dy[i]
        checkX = newX+dx[i]
        if 0 <= checkY < n and 0 <= checkX < m and vi[checkY][checkX]:
            vi[checkY][checkX] = False
            tetris(checkY,checkX,res+li[checkY][checkX],cnt+1)
            vi[checkY][checkX] = True
ans = 0
vi = list([True] * m for _ in range(n))
for y in range(n):
    for x in range(m):
        tetris(y,x,0,0)
print(ans)