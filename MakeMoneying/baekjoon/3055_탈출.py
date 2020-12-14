import sys
sys.stdin = open("3055in.txt",'r')

from collections import deque
R,C = map(int,input().split())
List = list(list( x for x in input()) for _ in range(R))
waters = deque([])
hedgehog = deque([])
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for y in range(R):
    for x in range(C):
        if List[y][x] == "*":
            waters.append((y,x))
        elif List[y][x] == "S":
            hedgehog.append((y,x))

cnt = 0
def fillWaters(y,x):
    global visitedWater
    for i in range(4):
        checkY = y+dy[i]
        checkX = x+dx[i]
        if 0<=checkY<R and 0<=checkX<C and visitedWater[checkY][checkX] and (List[checkY][checkX]=="." or List[checkY][checkX]=="S"):
            List[checkY][checkX]="*"
            waters.append((checkY,checkX))

def goBeaver(y,x):

    pass

visitedWater = list(list(True for _ in range(C)) for _ in range(R))
visitedBeaver = list(list(True for _ in range(C)) for _ in range(R))
answer = 0
flag = 1
while flag:
    answer += 1
    for _ in range(len(waters)):
        Y,X = waters.popleft()
        fillWaters(Y,X)
    for _ in range(len(hedgehog)):
        Y,X = hedgehog.popleft()
        for i in range(4):
            newY = Y + dy[i]
            newX = X + dx[i]
            if 0<=newY<R and 0<=newX<C and visitedBeaver[newY][newX]:
                visitedBeaver[newY][newX] = False
                if List[newY][newX] == ".":
                    List[newY][newX] = "S"
                    hedgehog.append((newY,newX))
                if List[newY][newX] == "D":
                    hedgehog.append(("end"))
                    flag = 0
                    break

    if len(hedgehog):
        pass
    else:
        break
if hedgehog:
    print(answer)
else:
    print("KAKTUS")