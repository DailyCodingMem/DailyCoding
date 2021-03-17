import sys
sys.stdin = open("3190in.txt",'r')

import sys
from collections import deque
dy = [0,1,0,-1]
dx = [1,0,-1,0]
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
li = list(list(0 for _ in range(n)) for _ in range(n))
vi = list(list(True for _ in range(n)) for _ in range(n))
for _ in range(k):
    y,x = map(int,sys.stdin.readline().split())
    li[y-1][x-1] = 1
timetable = []
for _ in range(int(sys.stdin.readline())):
    a,b = sys.stdin.readline().rstrip().split()
    timetable.append((int(a),b))
timetable = sorted(timetable, key=lambda x:int(-x[0]))
sy = sx = time = dir = 0
ba = deque([(sy,sx)])
while True:
    if time==172:
        print("hi")
    sy,sx = ba[-1]
    time += 1
    newY = sy+dy[dir]
    newX = sx+dx[dir]
    if not (0<=newY<n and 0<=newX<n):
        break
    vi[newY][newX] = False
    if not (newY,newX) in ba:
        ba.append((newY,newX))
    else:
        break
    if li[newY][newX]:
        li[newY][newX] = 0
        pass
    else:
        ba.popleft()
    if timetable and timetable[-1][0]==time:
        d = timetable[-1][1]
        if d =="L":
            dir = (dir+3)%4
        elif d =="D":
            dir = (dir+1)%4
        timetable.pop()
print(time)