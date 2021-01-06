import sys
sys.stdin = open("10026in.txt",'r')

N = int(input())
List = list(list( x for x in input()) for _ in range(N))
visited1 = list(list(True for _ in range(N)) for _ in range(N))
visited2 = list(list(True for _ in range(N)) for _ in range(N))
dy = [-1,1,0,0]
dx = [0,0,-1,1]
answer1 = answer2 = 0
checkColor={}
checkColor["R"] = 1
checkColor["G"] = 1
checkColor["B"] = 0
for y in range(N):
    for x in range(N):
        if visited1[y][x]:
            answer1 += 1
            color = List[y][x]
            visited1[y][x] = False
            normal = [(y,x)]
            while normal:
                newY,newX = normal.pop()
                for i in range(4):
                    checkY = newY + dy[i]
                    checkX = newX + dx[i]
                    if 0<=checkY<N and 0<= checkX < N and visited1[checkY][checkX] and List[checkY][checkX] == color:
                        visited1[checkY][checkX] = False
                        normal.append((checkY,checkX))
        
        if visited2[y][x]:
            answer2 += 1
            color = checkColor[List[y][x]]
            visited2[y][x] = False
            adnormal = [(y,x)]
            while adnormal:
                newY,newX = adnormal.pop()
                for i in range(4):
                    checkY = newY + dy[i]
                    checkX = newX + dx[i]
                    if 0<= checkY < N and 0<= checkX < N and visited2[checkY][checkX] and checkColor[List[checkY][checkX]] == color:
                        visited2[checkY][checkX] = False
                        adnormal.append((checkY,checkX))
print(answer1,answer2)