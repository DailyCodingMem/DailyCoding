import sys
sys.stdin = open("9328in.txt",'r')

from collections import deque
def go(checkY,checkX):
    global answer
    road = deque([(checkY,checkX)])
    while road:
        y,x = road.popleft()
        for i in range(4):
            newY = y+dy[i]
            newX = x+dx[i]
            if 0<=newY<h and 0<=newX<w and visited[newY][newX] and not maze[newY][newX] =="*":
                visited[newY][newX] = False
                if maze[newY][newX]==".":
                    road.append((newY,newX))
                elif maze[newY][newX]=="$":
                    road.append((newY,newX))
                    answer += 1
                else:
                    if 65<= ord(maze[newY][newX])<=90:
                        doors.append((maze[newY][newX],newY,newX))
                    else:
                        keyBox.append(maze[newY][newX])
                        road.append((newY,newX))
dy = [-1,1,0,0]
dx = [0,0,-1,1]
T = int(input())
for count in range(T):
    h,w = map(int,input().split())
    maze = list(list(x for x in input()) for _ in range(h))
    doors = []
    keyBox = deque(list(x for x in input())) #['c', 'z']
    if '0' in keyBox:
        keyBox = deque([])
    visited = list(list(True for _ in range(w)) for _ in range(h) )
    enter = deque([]) #deque([(1, 0), (2, 16)])
    answer = 0
    for i in range(w):
        visited[0][i] = False
        visited[h-1][i] = False
        if not maze[0][i]=="*":
            enter.append((0,i))
            if maze[0][i]=="$":
                answer += 1
            elif not maze[0][i]==".":
                if ord(maze[0][i])<=90: # 열쇠이면
                    doors.append((maze[0][i],0,i))
                    enter.pop()
                else:
                    keyBox.append(maze[0][i])
        if not maze[h-1][i]=="*":
            enter.append((h-1,i))
            if maze[h-1][i]=="$":
                answer += 1
            elif not maze[h-1][i]==".":
                if ord(maze[h-1][i])<=90:
                    doors.append((maze[h-1][i],h-1,i))
                    enter.pop() 
                else:
                    keyBox.append(maze[h-1][i])
    for j in range(1,h-1):
        visited[j][0] = False
        visited[j][w-1] = False
        if not maze[j][0]=="*":
            enter.append((j,0))
            if maze[j][0]=="$":
                answer += 1
            elif not maze[j][0]==".":
                if ord(maze[j][0])<=90:
                    doors.append((maze[j][0],j,0))
                    enter.pop()
                else:
                    keyBox.append(maze[j][0])
        if not maze[j][w-1]=="*":
            enter.append((j,w-1))
            if maze[j][w-1]=="$":
                answer += 1
            elif not maze[j][w-1]==".":
                if ord(maze[j][w-1])<=90:
                    doors.append((maze[j][w-1],j,w-1))
                    enter.pop()
                else:
                    keyBox.append(maze[j][w-1])

    for keyY,keyX in enter:
        go(keyY,keyX)
    while True:
        flag = 1
        for _ in range(len(keyBox)):
            key = keyBox.popleft()
            for _ in range(len(doors)):
                door,locY,locX = doors.pop(0)
                if ord(key)==ord(door)+32:
                    flag = 0
                    # print(door,"풀렸다. 위치는",locY,locX)
                    go(locY,locX)
                else:
                    doors.append((door,locY,locX))
            keyBox.append(key)
                
        if flag:
            break
    print(answer)
    # print(keyBox)
    # print("문은",doors)