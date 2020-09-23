import sys
sys.stdin = open("in.txt",'r')

n,m = map(int,input().split())
List = [list(map(int,input().split())) for _ in range(m)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]
visited = [[ True for _ in range(n)] for _ in range(m) ]
def Miro(y,x,val,cnt):
    global answer
    visited[y][x] = False
    if y == m and x == n:
        if Min > cnt:
            answer = Min
            return cnt
    
    answer += 1
    for i in range(4):
        Y = y+dy[i]
        X = x+dx[i]
        if 0<=Y<m and 0<=X<n and abs(List[Y][X]-val) <=1 and visited[Y][X]:
            return Miro(Y,X,List[Y][X],cnt+1)



answer = 1
Min = 1000000
Miro(0,0,List[0][0],1)
print(Miro(0,0,List[0][0],1))
print(answer)
print(Min)
