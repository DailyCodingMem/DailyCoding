import sys
sys.stdin = open("in.txt",'r')

dy = [-1,-1,-1,0,0,1,1,1]
dx = [-1,0,1,-1,1,-1,0,1]
def Omoc(y,x,color,direct):
    global cnt
    Y = y+dy[direct]
    X = x+dx[direct]
    if 0<=Y<19 and 0<=X<19 and List[Y][X]==color and (not i in check[Y][X]):
        check[Y][X].append(i)
        cnt += 1
        Omoc(Y,X,color,i)

check = [[[] for _ in range(19)] for _ in range(19)]

List = [list(map(int,input().split())) for _ in range(19)]
answer = []
for y in range(19):
    for x in range(19):
        if List[y][x]:
            color = List[y][x]
            for i in range(8):
                Y = y+dy[i]
                X = x+dx[i]
                
                if 0<=Y<19 and 0<=X<19 and List[Y][X]==color and (not i in check[Y][X]):
                    check[y][x].append(i)
                    check[Y][X].append(i)
                    cnt = 2
                    Omoc(Y,X,color,i)
                    if cnt == 5:
                        answer.append((color,(y+1,x+1)))
                        answer.append((color,(y+4*dy[i]+1,x+4*dx[i]+1)))
            else:
                List[y][x] = 0

if len(answer):
    answer = sorted(answer, key=lambda x: x[1][1])
    print(answer[0][0])
    print("{} {}".format(answer[0][1][0],answer[0][1][1]))
else:
    print(0)