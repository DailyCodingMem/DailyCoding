import sys
sys.stdin = open("in.txt",'r')

N = int(input())
List = [ [ int(x) for x in input() ] for x in range(N) ]

dy = [-1,1,0,0]
dx = [0,0,-1,1]
def Miro(Y,X):
    global result
    result += 1
    List[Y][X] = 0
    for i in range(4):
        newY = Y+dy[i]
        newX = X+dx[i]
        if 0<=newY<N and 0<=newX<N and List[newY][newX]:
            Miro(newY,newX)

basket = []
for Y in range(N):
    for X in range(N):
        if List[Y][X]:
            result = 0
            Miro(Y,X)
            basket.append(result)
basket.sort()
print(len(basket))
for i in basket:
    print(i)