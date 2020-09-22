import sys
sys.stdin = open("in.txt",'r')



def Lake(y,x):
    for i in range(8):
        Y = y+dy[i]
        X = x+dx[i]
        if 0<=Y<H and 0<=X<W and List[Y][X]=="L":
            List[Y][X] = "."
            Lake(Y,X)

dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]
W,H = map(int,input().split())
List = list( list(input().split()) for _ in range(H) )
answer = 0
for y in range(H):
    for x in range(W):
        if List[y][x] == "L":
            List[y][x] = "."
            answer += 1
            stack = [(y,x)]
            while stack:
                newY,newX = stack.pop(0)
                for i in range(8):
                    Y = newY+dy[i]
                    X = newX+dx[i]
                    if 0<=Y<H and 0<=X<W and List[Y][X]=="L":
                        List[Y][X] = "."
                        stack.append((Y,X))
print(answer)



